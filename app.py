import json
import os
import streamlit as st
import pandas as pd

from models.model_registry import MODELS
from sustainability.energy_estimator import estimate_energy_advanced
from sustainability.carbon_estimator import lifecycle_carbon
from sustainability.sustainability_score import advanced_sustainability_index
from utils.visualization import plot_pareto
from optimization.automl_selector import automl_search
from sustainability.energy_explain import energy_breakdown



# ---------------- Page Config ----------------
st.set_page_config(page_title="Green AI Model Selector", layout="wide")
st.title("🌱 Energy- & Carbon-Aware Model Selection Framework")

# ---------------- Sidebar ----------------
st.sidebar.header("⚙ Sustainability Preferences")

weights = {
    "accuracy": st.sidebar.slider("Accuracy Weight", 0.0, 1.0, 0.4),
    "energy": st.sidebar.slider("Energy Weight", 0.0, 1.0, 0.3),
    "carbon": st.sidebar.slider("Carbon Weight", 0.0, 1.0, 0.2),
    "latency": st.sidebar.slider("Latency Weight", 0.0, 1.0, 0.1),
}

scenario = st.sidebar.radio(
    "Deployment Scenario",
    ["Edge Device", "Cloud GPU", "On-Prem CPU"]
)

hardware_map = {
    "Edge Device": "Edge",
    "Cloud GPU": "GPU",
    "On-Prem CPU": "CPU"
}

hardware = hardware_map[scenario]
carbon_intensity = st.sidebar.slider("Carbon Intensity (gCO₂/kWh)", 100, 800, 475)
batch_size = st.sidebar.slider("Batch Size", 1, 64, 1)

# ---------------- Inference Computation ----------------
results = []

for model in MODELS:
    energy_infer = estimate_energy_advanced(
        model["flops"], hardware, batch_size
    )

    energy_train_est = energy_infer * 50  # fallback if no training file

    carbon = lifecycle_carbon(
        energy_train_est, energy_infer, carbon_intensity
    )

    results.append({
        "Model": model["name"],
        "Accuracy": model["accuracy"],
        "Energy (J)": round(energy_infer, 2),
        "Carbon (gCO₂)": round(carbon, 4),
        "Latency (ms)": model["latency"],
        "training_energy_J": 0.0  # default
    })

df = pd.DataFrame(results)


# ---------------- Total Energy ----------------
df["Total Energy (J)"] = df["Energy (J)"] + df["training_energy_J"]

# ---------------- Normalization ----------------
stats = {
    "acc_min": df["Accuracy"].min(),
    "acc_max": df["Accuracy"].max(),
    "energy_min": df["Total Energy (J)"].min(),
    "energy_max": df["Total Energy (J)"].max(),
    "carbon_min": df["Carbon (gCO₂)"].min(),
    "carbon_max": df["Carbon (gCO₂)"].max(),
    "lat_min": df["Latency (ms)"].min(),
    "lat_max": df["Latency (ms)"].max(),
}

df["Sustainability Score"] = df.apply(
    lambda row: advanced_sustainability_index(
        {
            "accuracy": row["Accuracy"],
            "energy": row["Total Energy (J)"],
            "carbon": row["Carbon (gCO₂)"],
            "latency": row["Latency (ms)"],
        },
        stats,
        weights
    ),
    axis=1
)

# ---------------- Main Table ----------------
st.subheader("📊 Model Sustainability Comparison")
st.dataframe(df, use_container_width=True)

best_model = df.sort_values(
    "Sustainability Score", ascending=False
).iloc[0]

st.subheader("🏆 Recommended Sustainable Model")
st.success(best_model["Model"])

# ---------------- Pareto Frontier ----------------
st.subheader("📈 Pareto Frontier (Accuracy vs Energy)")
st.pyplot(plot_pareto(df))

# ---------------- Energy Breakdown ----------------
st.subheader("🧠 Explainable Energy Attribution")

energy_parts = energy_breakdown(best_model)

st.bar_chart(
    pd.DataFrame.from_dict(
        energy_parts, orient="index", columns=["Energy (J)"]
    )
)

# ---------------- AutoML Search ----------------
st.subheader("🤖 AutoML Energy-Constrained Model Selection")

budget = st.slider("Energy Budget (J)", 100, int(df["Total Energy (J)"].max()), 3000)

automl_model = automl_search(
    df.to_dict(orient="records"),
    budget
)

if automl_model:
    st.success(f"AutoML Selected Model: {automl_model['Model']}")
else:
    st.warning("No model fits the selected energy budget.")



# ---------------- Explanation ----------------
st.info(
    f"""
    **{best_model['Model']}** was selected because it:
    - Maximizes sustainability score
    - Minimizes lifecycle energy consumption
    - Produces lower carbon emissions
    - Performs well under **{scenario}**
    """
)