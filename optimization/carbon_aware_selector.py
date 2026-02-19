def carbon_aware_switch(models, carbon_intensity, threshold=500):
    """
    Switch models based on grid carbon intensity
    """
    if carbon_intensity > threshold:
        # Prefer lightweight models
        return min(models, key=lambda x: x["energy"])
    else:
        # Prefer accuracy
        return max(models, key=lambda x: x["accuracy"])
