from core.microscope_data import MICROSCOPES
from core.calculator import calculate_real_size
from core.database import create_table
from core.database import save_record
from core.database import get_records


create_table()


def main():

    print("Microscope Specimen Size Calculator")

    username = input("Enter username: ")

    measured_size = float(
        input("Enter measured size in mm: ")
    )

    microscope_names = list(MICROSCOPES.keys())

    print("\nSelect Microscope:")

    for i, microscope in enumerate(microscope_names, start=1):
        print(f"{i}. {microscope}")

    choice = int(input("Enter choice: "))

    microscope_type = microscope_names[choice - 1]

    magnification = MICROSCOPES[microscope_type]

    print("\nOutput Units")
    print("1. nm")
    print("2. um")
    print("3. mm")
    print("4. cm")
    print("5. m")

    unit_choice = int(input("Enter unit choice: "))

    unit_map = {
        1: "nm",
        2: "um",
        3: "mm",
        4: "cm",
        5: "m"
    }

    output_unit = unit_map[unit_choice]

    real_size_mm, converted = calculate_real_size(
        measured_size,
        magnification,
        output_unit
    )

    print("\n--- RESULT ---")

    print(f"Real Size: {converted} {output_unit}")

    save_record(
        username,
        measured_size,
        microscope_type,
        magnification,
        converted,
        output_unit
    )

    print("\n--- HISTORY ---")

    records = get_records()

    for record in records:
        print(record)


if __name__ == "__main__":
    main()