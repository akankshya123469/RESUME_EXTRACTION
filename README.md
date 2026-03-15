Resume Entity Extraction Pipeline
Overview

This project implements a Python-based Resume Entity Extraction pipeline that converts resumes and professional profiles into structured JSON data.

The system processes resumes from multiple formats and extracts key candidate information such as:

Name

Skills

Education

Companies

Experience

Projects

The extracted data is returned in a structured JSON format, enabling use cases like:

Candidate search

Resume ranking

Talent analytics

🎯 Objective

The goal of the project is to build a flexible resume processing pipeline that:

✔ Accepts resumes from different sources
✔ Extracts important candidate information
✔ Handles both text-based and scanned resumes
✔ Produces structured JSON output

📥 Supported Input Types

The pipeline supports multiple input sources:

1️⃣ Resume Files

Supported formats:

PDF (Text-based)

PDF (Scanned)

DOCX

TXT

Processing methods:

File Type	Method Used
Text PDF	PyMuPDF parser
Scanned PDF	OCR using Tesseract
DOCX	python-docx parser
2️⃣ LinkedIn Profile URL

The pipeline can accept a LinkedIn profile link and extract:

Name

Experience

Skills

Education

Companies

Projects

(Note: LinkedIn extraction depends on publicly available profile content.)

3️⃣ Google Drive Resume Links

The system can download resumes directly from Google Drive links and process them.

4️⃣ Direct Resume Text

Users can also paste resume text directly into the pipeline.

⚙️ System Architecture

The pipeline consists of multiple stages:

Resume Input
     ↓
Input Detection
     ↓
Document Parsing / OCR
     ↓
Text Cleaning
     ↓
Entity Extraction
     ↓
JSON Output
🧠 Entity Extraction Approach

This project uses a Hybrid Entity Extraction approach combining:

1️⃣ Named Entity Recognition (NER)

Used for extracting:

Person names

Organization names

Implemented using:

spaCy pre-trained NLP model

2️⃣ NLP Token Analysis

Used for extracting:

Skills

Technical terms

Relevant keywords

Implemented using:

spaCy token analysis

POS tagging

3️⃣ Rule-Based Extraction

Used for detecting structured resume sections such as:

Education

Projects

Experience

Implemented using:

Regex pattern matching

Section keyword detection

4️⃣ OCR for Scanned Resumes

Scanned resumes are processed using:

Tesseract OCR

This converts image-based PDFs into machine-readable text.

🛠️ Technology Stack
Programming Language

Python

Document Processing

PyMuPDF

python-docx

OCR

Tesseract OCR

Pillow

NLP / Entity Extraction

spaCy

Regex

Token analysis

Data Handling

Python

JSON

📂 Project Structure
resume_extraction
│
├── sample_resumes
│   ├ resume1.pdf
│   └ resume2.docx
│
├── input_processing
│   ├ pdf_parser.py
│   ├ ocr_engine.py
│   ├ docx_parser.py
│   ├ linkedin_parser.py
│   └ gdrive_downloader.py
│
├── entity_extraction
│   ├ ner_model.py
│   ├ skills_extractor.py
│   ├ education_extractor.py
│   ├ projects_extractor.py
│   └ experience_extractor.py
│
├── utils
│   └ text_cleaner.py
│
├── pipeline
│   └ main_pipeline.py
│
├── output
│   └ json_formatter.py
│
├── requirements.txt
└── README.md
📊 Output Format

The extracted information is returned in the following JSON format:

{
"name": "John Doe",
"skills": ["Python", "Machine Learning", "SQL"],
"education": ["B.Tech Computer Science - XYZ University"],
"companies": ["Google", "Amazon"],
"experience_years": "5",
"projects": ["Fraud Detection System", "Recommendation Engine"]
}
🚀 Installation
1️⃣ Clone the repository
git clone <repository-url>
cd resume_extraction
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Install spaCy model
python -m spacy download en_core_web_sm
4️⃣ Install Tesseract OCR

Download from:

https://github.com/tesseract-ocr/tesseract

Add it to your system PATH.

▶️ Running the Pipeline

Run the pipeline using:

python -m pipeline.main_pipeline

The system will process the sample resume and output extracted JSON data.

🧪 Sample Test Cases

The system was tested on:

Text-based PDF resumes

Scanned PDF resumes

DOCX resumes

LinkedIn profile input

⚠️ Limitations

Accuracy depends on resume formatting

LinkedIn scraping may be restricted

Skills extraction may include noisy tokens

OCR accuracy depends on scan quality

🔮 Future Improvements

Possible enhancements include:

Transformer-based NER models

Skill ontology matching

Resume ranking system

Web interface using Streamlit

REST API using FastAPI

👩‍💻 Author

Akankshya Dash

Computer Science (Data Science)
Siksha 'O' Anusandhan University
