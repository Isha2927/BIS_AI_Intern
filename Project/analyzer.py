from reference_ranges import REFERENCE_RANGES

def analyze_report(data):

    results = []

    for item in data:

        test_name = item["test_name"]

        try:
            value = float(item["value"])
        except:
            continue

        if test_name in REFERENCE_RANGES:

            low, high = REFERENCE_RANGES[test_name]

            if value < low:
                status = "LOW"

            elif value > high:
                status = "HIGH"

            else:
                status = "NORMAL"

            results.append({
                "test_name": test_name,
                "value": value,
                "status": status,
                "normal_range": f"{low}-{high}"
            })

    return results