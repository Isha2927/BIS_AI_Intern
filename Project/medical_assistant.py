import os
import json

from extract import extract_text
from document_classifier import classify_document

# Lab Report Modules
from smart_parser import extract_medical_parameters
from analyzer import analyze_report
from report_generator import generate_summary
from explanation_engine import generate_explanations

# Prescription Module
from medicine_lookup import lookup_medicine


# ==========================================
# INPUT IMAGE
# ==========================================

image_path = input("Enter image path: ")

if not os.path.exists(image_path):
    print("Error: File not found.")
    exit()

print("\n===== EXTRACTING TEXT =====\n")

text = extract_text(image_path)

print(text)

# ==========================================
# DOCUMENT CLASSIFICATION
# ==========================================

document_type = classify_document(text)

print(f"\n===== DOCUMENT TYPE =====")
print(document_type)

# ==========================================
# LAB REPORT PIPELINE
# ==========================================

if document_type == "Lab Report":

    print("\n===== PROCESSING LAB REPORT =====\n")

    # Extract Parameters
    data = extract_medical_parameters(text)

    print("===== EXTRACTED PARAMETERS =====\n")

    for item in data:
        print(item)

    # Analyze Parameters
    analysis = analyze_report(data)

    print("\n===== ANALYSIS =====\n")

    for item in analysis:
        print(item)

    # Summary
    print("\n===== MEDICAL REPORT SUMMARY =====\n")

    generate_summary(analysis)

    # Explanations
    print("\n===== EXPLANATIONS =====\n")

    explanations = generate_explanations(analysis)

    for item in explanations:

        print(f"\nTest: {item['test_name']}")
        print(f"Status: {item['status']}")
        print(f"Description: {item['description']}")
        print(f"Interpretation: {item['meaning']}")

    # Overall Insights
    print("\n===== OVERALL REPORT INSIGHTS =====\n")

    high_count = sum(
        1 for item in analysis
        if item["status"] == "HIGH"
    )

    low_count = sum(
        1 for item in analysis
        if item["status"] == "LOW"
    )

    normal_count = sum(
        1 for item in analysis
        if item["status"] == "NORMAL"
    )

    print(f"High Parameters   : {high_count}")
    print(f"Low Parameters    : {low_count}")
    print(f"Normal Parameters : {normal_count}")
    print(f"Total Anomalies   : {high_count + low_count}")

    # Save JSON
    os.makedirs("outputs", exist_ok=True)

    with open(
        "outputs/report_results.json",
        "w"
    ) as f:

        json.dump(
            analysis,
            f,
            indent=4
        )

    print(
        "\nJSON saved at: outputs/report_results.json"
    )

# ==========================================
# PRESCRIPTION PIPELINE
# ==========================================

elif document_type == "Prescription":

    print("\n===== PROCESSING PRESCRIPTION =====\n")

    medicine_name = text.strip().split("\n")[0]

    print(f"Detected Medicine: {medicine_name}")

    result = lookup_medicine(medicine_name)

    if result:

        print("\n===== MEDICINE INFORMATION =====\n")

        print(
            f"Medicine Name : {result['medicine']}"
        )

        print(
            f"Generic Name  : {result['generic_name']}"
        )

        print(
            f"Category      : {result['category']}"
        )

        print(
            f"Use           : {result['use']}"
        )

        os.makedirs("outputs", exist_ok=True)

        with open(
            "outputs/prescription_results.json",
            "w"
        ) as f:

            json.dump(
                result,
                f,
                indent=4
            )

        print(
            "\nJSON saved at: outputs/prescription_results.json"
        )

    else:

        print("Medicine not found.")

# ==========================================
# UNKNOWN DOCUMENT
# ==========================================

else:

    print(
        "Unable to determine document type."
    )

print("\n===== PROCESS COMPLETED =====")