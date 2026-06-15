import re

def extract_medical_parameters(text):

    lines = text.split("\n")

    extracted = []

    pattern = r'([A-Za-z0-9+\-\(\)\s]+)\s+([\d.]+)\s*([A-Za-z/%]+)?'

    for line in lines:

        line = line.strip()

        match = re.search(pattern, line)

        if match:

            test_name = match.group(1).strip()
            value = match.group(2)

            unit = ""
            if match.group(3):
                unit = match.group(3)

            extracted.append({
                "test_name": test_name,
                "value": value,
                "unit": unit
            })

    return extracted