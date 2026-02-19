import matplotlib.pyplot as plt

def plot_pareto(df):
    plt.figure()
    plt.scatter(df["Energy (J)"], df["Accuracy"])
    plt.xlabel("Energy (J)")
    plt.ylabel("Accuracy")
    plt.title("Pareto Frontier: Accuracy vs Energy")
    return plt
