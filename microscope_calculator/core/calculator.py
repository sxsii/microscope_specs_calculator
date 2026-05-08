UNIT_CONVERSION = {
    "nm": 1_000_000,
    "um": 1000,
    "mm": 1,
    "cm": 0.1,
    "m": 0.001
}


def calculate_real_size(measured_size_mm, magnification, output_unit):

    if measured_size_mm <= 0:
        raise ValueError("Measured size must be positive")

    real_size_mm = measured_size_mm / magnification

    converted = real_size_mm * UNIT_CONVERSION[output_unit]

    return real_size_mm, converted