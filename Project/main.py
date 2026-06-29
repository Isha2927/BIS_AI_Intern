import os

from extract import extract_text
from smart_parser import extract_medical_parameters
from analyzer import analyze_report
from report_generator import generate_summary
from dataframe_handler import create_dataframe


def main():

    # Report image path
    image_path = r"Report/MUM-0125-PA-0001141_W2500438UNADKAT ASHWIN_27-04-2025_1002-19_AM.pdf_page_114.png"

    print("\n===== STARTING MEDICAL REPORT ANALYSIS =====\n")

    # STEP 1: OCR Extraction
    text = extract_text(image_path)

    print("\n===== OCR TEXT EXTRACTED =====\n")
    # Uncomment below if you want to see full OCR text
    # print(text)
    from document_classifier import classify_document

    document_type = classify_document(text)
    print("\n===== DOCUMENT TYPE =====")
    print(document_type)
    # STEP 2: Medical Parameter Extraction
    data = extract_medical_parameters(text)

    print("\n===== EXTRACTED PARAMETERS =====\n")

    if not data:
        print("No medical parameters found.")
    else:
        for item in data:
            print(item)

    # STEP 3: Analysis
    analysis = analyze_report(data)

    print("\n===== ANALYSIS =====\n")

    if not analysis:
        print("No analyzable parameters found.")
    else:
        for item in analysis:
            print(item)

    # STEP 4: Summary Generation
    print("\n===== MEDICAL REPORT SUMMARY =====\n")
    generate_summary(analysis)
    

    from explanation_engine import generate_explanations

    

    print("\n===== EXPLANATIONS =====\n")

    explanations = generate_explanations(analysis)

    for item in explanations:
        print(f"\nTest: {item['test_name']}")
        print(f"Status: {item['status']}")
        print(f"Description: {item['description']}")
        print(f"Interpretation: {item['meaning']}")


    # STEP 5: Create DataFrame
    df = create_dataframe(analysis)

    print("\n===== DATAFRAME =====\n")
    print(df)

    # STEP 6: Create output folder automatically
    os.makedirs("outputs", exist_ok=True)

    # STEP 7: Save CSV
    output_file = "outputs/report_analysis.csv"

    df.to_csv(output_file, index=False)

    print(f"\nCSV saved successfully at: {output_file}")

    print("\n===== PROCESS COMPLETED SUCCESSFULLY =====\n")


if __name__ == "__main__":
    main()