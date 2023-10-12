import streamlit as st
from docx import Document

# Define the function to generate the document draft
def generate_document_draft(language, document_type, details):
    # Define the templates for the loan and rental agreements in English and Hindi
    templates = {
        "English": {
            "Loan Agreement": """
            LOAN AGREEMENT

            This Loan Agreement (the "Agreement") is entered into on [Repayment Start Date], between:

            1. Lender:
               - Name: [Lender's Full Name]
               - Address: [Lender's Address]
               - Phone: [Lender's Phone Number]
               - Email: [Lender's Email Address]

            2. Borrower:
               - Name: [Borrower's Full Name]
               - Address: [Borrower's Address]
               - Phone: [Borrower's Phone Number]
               - Email: [Borrower's Email Address]

            3. Loan Details:
               - Loan Amount: [Loan Amount] INR
               - Interest Rate: [Interest Rate]
               - Loan Term: [Loan Term] months
               - Repayment Schedule: [Repayment Schedule]
               - Payment Amount: [Payment Amount] INR
               - Interest Calculation Method: [Interest Calculation Method]
               - Prepayment Penalty: [Prepayment Penalty]
               - Default Events: [Default Events]
               - Default Remedies: [Default Remedies]
               - Governing Law and Jurisdiction: [Governing Law]

            4. Terms and Conditions:
               [Add terms and conditions here]

            IN WITNESS WHEREOF, the parties hereto have executed this Agreement as of the date first above written.

            Lender:
            [Signature]                                       [Date]

            Borrower:
            [Signature]                                       [Date]
            """,
            "Rental Agreement": """
            RENTAL AGREEMENT

            This Rental Agreement (the "Agreement") is entered into on [Rental Start Date], between:

            1. Landlord:
               - Name: [Landlord's Full Name]
               - Address: [Landlord's Address]
               - Phone: [Landlord's Phone Number]
               - Email: [Landlord's Email Address]

            2. Tenant:
               - Name: [Tenant's Full Name]
               - Address: [Tenant's Address]
               - Phone: [Tenant's Phone Number]
               - Email: [Tenant's Email Address]

            3. Property Details:
               - Property Address: [Property Address]
               - Monthly Rent: [Monthly Rent] INR
               - Lease Term: [Lease Term] months
               - Security Deposit: [Security Deposit] INR

            4. Terms and Conditions:
               [Add terms and conditions here]

            IN WITNESS WHEREOF, the parties hereto have executed this Agreement as of the date first above written.

            Landlord:
            [Signature]                                       [Date]

            Tenant:
            [Signature]                                       [Date]
            """
        },
        "Hindi": {
            "Loan Agreement": """
            ऋण समझौता

            इस ऋण समझौते (यह "समझौता") को [पुनर्भुगतान प्रारंभ तिथि] को निम्नलिखित द्वारा किया जाता है:

            1. प्रधान:
               - नाम: [प्रधान का पूरा नाम]
               - पता: [प्रधान का पता]
               - फ़ोन: [प्रधान का फ़ोन नंबर]
               - ईमेल: [प्रधान का ईमेल पता]

            2. उधारक:
               - नाम: [उधारक का पूरा नाम]
               - पता: [उधारक का पता]
               - फ़ोन: [उधारक का फ़ोन नंबर]
               - ईमेल: [उधारक का ईमेल पता]

            3. ऋण विवरण:
               - ऋण राशि: [ऋण राशि] INR
               - ब्याज दर: [ब्याज दर]
               - ऋण अवधि: [ऋण अवधि] महीने
               - पुनर्भुगतान कार्यक्रम: [पुनर्भुगतान कार्यक्रम]
               - भुगतान राशि: [भुगतान राशि] INR
               - ब्याज गणना विधि: [ब्याज गणना विधि]
               - पूर्व-भुगतान जुर्माना: [पूर्व-भुगतान जुर्माना]
               - डिफ़ॉल्ट घटनाएँ: [डिफ़ॉल्ट घटनाएँ]
               - डिफ़ॉल्ट उपाय: [डिफ़ॉल्ट उपाय]
               - शासकीय कानून और प्राधिकृति: [शासकीय कानून]

            4. नियम और शर्तें:
               [यहां नियम और शर्तें जोड़ें]

            जिस साक्षर बनाने की दिनांक के रूप में इस पर पार्टियों ने इस समझौते को किया है।

            प्रधान:
            [हस्ताक्षर]                                       [तिथि]

            उधारक:
            [हस्ताक्षर]                                       [तिथि]
            """,
            "Rental Agreement": """
            किराया समझौता

            इस किराया समझौते (यह "समझौता") को [किराया प्रारंभ तिथि] को निम्नलिखित द्वारा किया जाता है:

            1. मालिक:
               - नाम: [मालिक का पूरा नाम]
               - पता: [मालिक का पता]
               - फ़ोन: [मालिक का फ़ोन नंबर]
               - ईमेल: [मालिक का ईमेल पता]

            2. किरायेदार:
               - नाम: [किरायेदार का पूरा नाम]
               - पता: [किरायेदार का पता]
               - फ़ोन: [किरायेदार का फ़ोन नंबर]
               - ईमेल: [किरायेदार का ईमेल पता]

            3. संपत्ति विवरण:
               - संपत्ति पता: [संपत्ति पता]
               - मासिक किराया: [मासिक किराया] INR
               - किराये की अवधि: [किराये की अवधि] महीने
               - सुरक्षा जमा: [सुरक्षा जमा] INR

            4. नियम और शर्तें:
               [यहां नियम और शर्तें जोड़ें]

            जिस साक्षर बनाने की दिनांक के रूप में इस पर पार्टियों ने इस समझौते को किया है।

            मालिक:
            [हस्ताक्षर]                                       [तिथि]

            किरायेदार:
            [हस्ताक्षर]                                       [तिथि]
            """
        },
    }

    # Get the selected template based on the language and document type
    template = templates[language][document_type]

    # Replace placeholders with user-provided details
    for key, value in details.items():
        template = template.replace(f"[{key}]", value)

    return template

# Streamlit app
st.title("Legal Document Generator")

# Login Page
login = st.sidebar.checkbox("Login")
if login:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

# Consult a Lawyer Page
st.sidebar.subheader("Consult a Lawyer")
st.sidebar.write("Lawyer: John Doe")
st.sidebar.write("Contact: john.doe@example.com")

# Chat with AI Page
st.sidebar.subheader("Chat with AI")

# Generate Legal Documents Page
st.sidebar.subheader("Generate Legal Documents")

document_type = st.selectbox("Select Document Type", ["Loan Agreement", "Rental Agreement"])
language = st.selectbox("Select Language", ["English", "Hindi"])
st.subheader(f"Generate {document_type} in {language}")

details = {}  # Create an empty dictionary to store user input

# Define placeholders for input fields with Indian names
if document_type == "Loan Agreement":
    placeholders = {
        "Lender's Full Name": "प्रधान का पूरा नाम",
        "Lender's Address": "प्रधान का पता",
        "Lender's Phone Number": "प्रधान का फ़ोन नंबर",
        "Lender's Email Address": "प्रधान का ईमेल पता",
        "Borrower's Full Name": "उधारक का पूरा नाम",
        "Borrower's Address": "उधारक का पता",
        "Borrower's Phone Number": "उधारक का फ़ोन नंबर",
        "Borrower's Email Address": "उधारक का ईमेल पता",
        "Loan Amount": "10000",
        "Interest Rate": "5%",
        "Loan Term": "36",
        "Repayment Schedule": "मासिक",
        "Payment Amount": "300",
        "Interest Calculation Method": "साधारण ब्याज",
        "Prepayment Penalty": "कोई नहीं",
        "Default Events": "विलंब भुगतान",
        "Default Remedies": "जुर्माने",
        "Governing Law": "कैलिफ़ोर्निया राज्य",
        "Signature": "प्रधान",
        "Date": "2023-10-10",
    }
else:
    placeholders = {
        "Landlord's Full Name": "मालिक का पूरा नाम",
        "Landlord's Address": "मालिक का पता",
        "Landlord's Phone Number": "मालिक का फ़ोन नंबर",
        "Landlord's Email Address": "मालिक का ईमेल पता",
        "Tenant's Full Name": "किरायेदार का पूरा नाम",
        "Tenant's Address": "किरायेदार का पता",
        "Tenant's Phone Number": "किरायेदार का फ़ोन नंबर",
        "Tenant's Email Address": "किरायेदार का ईमेल पता",
        "Property Address": "संपत्ति पता",
        "Monthly Rent": "1000",
        "Lease Term": "12",
        "Security Deposit": "1500",
        "Signature": "मालिक",
        "Date": "2023-10-10",
    }

# Create input fields dynamically
for key, placeholder in placeholders.items():
    if key == "Signature":
        details[key] = st.text_input(f"Enter {key}", placeholder, key=key)
    elif key == "Date":
        details[key] = st.date_input(f"Enter {key}", key=key)
    else:
        details[key] = st.text_input(f"Enter {key}", placeholder, key=key)

# Display a preview of the agreement
st.subheader("Agreement Preview:")
agreement_preview = generate_document_draft(language, document_type, details)
st.write(agreement_preview)

# Progress bar to indicate the percentage of the document filled
percentage_filled = (len(details) / len(placeholders)) * 100
st.sidebar.progress(percentage_filled / 100)

# Generate and display the agreement
if st.button("Generate Agreement"):
    document = generate_document_draft(language, document_type, details)
    st.subheader("Generated Agreement:")
    st.write(document)

# Provide a download link for the document
if "Signature" in details:
    filename = f"{document_type.replace(' ', '_')}_{details['Signature']}.docx"
else:
    filename = f"{document_type.replace(' ', '_')}_Document.docx"

with st.expander("Download Agreement"):
    st.write(f"Download your {document_type} document: [Download {document_type} Document]({filename})")
