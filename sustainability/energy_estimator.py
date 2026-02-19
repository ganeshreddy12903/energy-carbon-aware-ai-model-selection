def estimate_energy_advanced(flops, hardware="CPU", batch_size=1):
    """
    Advanced energy estimation considering workload
    """
    hardware_profiles = {
        "CPU": {"power": 50, "efficiency": 0.8},
        "GPU": {"power": 220, "efficiency": 1.3},
        "Edge": {"power": 15, "efficiency": 0.6}
    }

    profile = hardware_profiles[hardware]

    execution_time = (flops * batch_size) / (1e9 * profile["efficiency"])
    energy = execution_time * profile["power"]

    return energy
