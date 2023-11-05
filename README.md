# pip install python-docx
```
pip install python-docx
sudo apt-get install poppler-utils
```

## Package
- Flask
- Python-docx
- Pillow
- Requests
- Subprocess
- ABC
- os
- Argparse



## Project Diagram
```
MemeGeneratorProject/
│
├── MemeEngine/                  # Module for meme generation logic
│   ├── __init__.py
│   ├── MemeEngine.py            # Core meme generation functionality
│
│
├── fonts/                   # Directory for font files
│   ├── Calibri Bold.TTF
│   ├── Calibri Regular.ttf  
│   └── LilitaOne-Regular.ttf    
│
├── QuoteEngine/                 # Module for quote handling logic
│   ├── __init__.py
│   ├── IngestorInterface.py     # Interface for ingestors
│   ├── Ingestor.py              # Ingestor for handling different file types
│   ├── QuoteModel.py            # Model for quotes
│   ├── CSVIngestor.py           # Ingestor for CSV files
│   ├── DocxIngestor.py          # Ingestor for DOCX files
│   ├── PDFIngestor.py           # Ingestor for PDF files
│   └── TextIngestor.py          # Ingestor for text files
│
├── static/                      # Static files (images, CSS, JS)
│   ├── images/
│   └── styles/
│
├── templates/                   # HTML templates for the web interface
│   ├── base.html
│   ├── meme.html
│   └── meme_form.html
│
├── _data/                       # Data files (quotes, images)
│   ├── DogQuotes/
│   └── SimpleLines/
│   └── photos/dog/
│
├── app.py 
├── meme.py                      # Main application script
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```