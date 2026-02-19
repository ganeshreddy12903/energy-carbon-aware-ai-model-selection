def energy_breakdown(model):
    return {
        "Computation": model["Energy (J)"] * 0.6,
        "Memory": model["Energy (J)"] * 0.25,
        "Data Transfer": model["Energy (J)"] * 0.15
    }
