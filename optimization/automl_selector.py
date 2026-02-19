def automl_search(models, budget_energy):
    """
    Select best model under energy budget
    """
    feasible = [m for m in models if m["Energy (J)"] <= budget_energy]
    if not feasible:
        return None
    return max(feasible, key=lambda x: x["Accuracy"])
