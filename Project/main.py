from extract import extract_text
from smart_parser import extract_medical_parameters
from analyzer import analyze_report

image_path = r"Report/MUM-0125-PA-0001141_W2500438UNADKAT ASHWIN_27-04-2025_1002-19_AM.pdf_page_114.png"

# Step 1: OCR
text = extract_text(image_path)

# Step 2: Parse extracted text
data = extract_medical_parameters(text)

print("\nEXTRACTED PARAMETERS:\n")
for item in data:
    print(item)

# Step 3: Analyze report
analysis = analyze_report(data)

print("\nANALYSIS:\n")
for item in analysis:
    print(item)

from report_generator import generate_summary

generate_summary(analysis)

from dataframe_handler import create_dataframe

df = create_dataframe(analysis)

print("\nDATAFRAME\n")
print(df)

df.to_csv("outputs/report_analysis.csv", index=False)