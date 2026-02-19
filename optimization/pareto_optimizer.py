def pareto_filter(models):
    pareto_models = []

    for m in models:
        dominated = False
        for n in models:
            if (
                n["accuracy"] >= m["accuracy"] and
                n["energy"] <= m["energy"] and
                n["carbon"] <= m["carbon"] and
                n["latency"] <= m["latency"]
            ) and n != m:
                dominated = True
                break
        if not dominated:
            pareto_models.append(m)

    return pareto_models
