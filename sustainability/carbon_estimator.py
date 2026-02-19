def lifecycle_carbon(energy_train, energy_infer, carbon_intensity):
    """
    Total carbon footprint (training + inference)
    """
    total_energy = energy_train + energy_infer
    total_energy_kwh = total_energy / 3.6e6
    carbon = total_energy_kwh * carbon_intensity
    return carbon
