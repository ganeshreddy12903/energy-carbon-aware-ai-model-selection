def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val + 1e-9)


def advanced_sustainability_index(model, stats, weights):
    """
    Normalized multi-objective sustainability index
    """
    acc = normalize(model["accuracy"], stats["acc_min"], stats["acc_max"])
    energy = normalize(model["energy"], stats["energy_min"], stats["energy_max"])
    carbon = normalize(model["carbon"], stats["carbon_min"], stats["carbon_max"])
    latency = normalize(model["latency"], stats["lat_min"], stats["lat_max"])

    score = (
        weights["accuracy"] * acc
        - weights["energy"] * energy
        - weights["carbon"] * carbon
        - weights["latency"] * latency
    )

    return score
