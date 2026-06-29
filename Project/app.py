import streamlit as st
from rag import retrieve

from extract import extract_text
from document_classifier import classify_document

from smart_parser import extract_medical_parameters
from analyzer import analyze_report
from explanation_engine import generate_explanations

from medicine_lookup import lookup_medicine

st.set_page_config(
    page_title="Medical AI Assistant",
    page_icon="🏥"
)

st.title("🏥 Medical AI Assistant")

uploaded_file = st.file_uploader(
    "Upload Medical Report or Prescription",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image_path = f"temp_{uploaded_file.name}"

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(image_path, width=400)

    if st.button("Analyze Document"):

        text = extract_text(image_path)

        document_type = classify_document(text)

        st.success(f"Document Type: {document_type}")

        # ==========================
        # LAB REPORT
        # ==========================

        if document_type == "Lab Report":

            data = extract_medical_parameters(text)

            analysis = analyze_report(data)

            st.subheader("Medical Analysis")

            for item in analysis:

                st.write(
                    f"{item['test_name']} : {item['value']} ({item['status']})"
                )

            explanations = generate_explanations(
                analysis
            )

            st.subheader("Explanations")

            for item in explanations:

                st.write(
                    f"**{item['test_name']}**"
                )

                st.write(
                    item['description']
                )

                st.write(
                    item['meaning']
                )

                st.divider()

        # ==========================
        # PRESCRIPTION
        # ==========================

        elif document_type == "Prescription":

            medicine_name = text.strip().split("\n")[0]

            result = lookup_medicine(
                medicine_name
            )

            st.subheader("Medicine Information")

            if result:

                st.write(
                    f"Medicine: {result['medicine']}"
                )

                st.write(
                    f"Generic Name: {result['generic_name']}"
                )

                st.write(
                    f"Category: {result['category']}"
                )

                st.write(
                    f"Use: {result['use']}"
                )

            else:

                st.error(
                    "Medicine not found."
                )

st.header("Ask Medical Questions")

question = st.text_input(
    "Ask a question about the report or medicine"
)

if st.button("Get Answer"):

    results = retrieve(question)

    st.subheader("Answer")

    for r in results:
        st.write(r)