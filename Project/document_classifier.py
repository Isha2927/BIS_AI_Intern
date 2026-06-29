from medicine_lookup import lookup_medicine

def classify_document(text):

    text = text.lower()

    lab_keywords = [
        "hemoglobin",
        "wbc",
        "rbc",
        "platelet",
        "laboratory",
        "report",
        "test",
        "crp",
        "glucose",
        "cholesterol",
        "sample",
        "result",
        "reference range",
        "ph",
        "pco",
        "po",
        "lactate"
    ]

    lab_score = 0

    for word in lab_keywords:
        if word in text:
            lab_score += 1

    print(f"Lab Score: {lab_score}")

    # LAB REPORT
    if lab_score > 0:
        return "Lab Report"

    # PRESCRIPTION CHECK
    medicine = lookup_medicine(text.strip())

    if medicine:
        return "Prescription"

    return "Unknown"