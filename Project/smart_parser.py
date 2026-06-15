import re

def extract_medical_parameters(text):

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    results = []

    i = 0

    while i < len(lines) - 2:

        test_name = lines[i]

        value = lines[i + 1]

        unit = lines[i + 2]

        # Check if value is numeric
        if re.match(r'^\d+(\.\d+)?$', value):

            # Common medical units
            valid_units = [
                "mmHg",
                "mmol/L",
                "mmo/L",
                "mg/L",
                "%",
                "g/dL",
                "gm%",
                "Vol%",
                "uL"
            ]

            if any(u.lower() in unit.lower() for u in valid_units):

                results.append({
                    "test_name": test_name,
                    "value": value,
                    "unit": unit
                })

                i += 3
                continue

        i += 1

    return results