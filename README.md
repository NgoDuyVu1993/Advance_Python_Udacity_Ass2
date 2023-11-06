# Meme Generator

Run the Application Web Interface
```
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload
```
<img src="https://github.com/NgoDuyVu1993/Advance_Python_Udacity_Ass2/blob/main/test/Test_app.gif">

Run the Application Commandline
```
python3 meme.py --path _data/photos/dog/xander_1.jpg --body "I feel Blue" --author "mr peanutbutter"
```
<img src="https://github.com/NgoDuyVu1993/Advance_Python_Udacity_Ass2/blob/main/test/Test_app.gif">
<img src="https://github.com/NgoDuyVu1993/Advance_Python_Udacity_Ass2/tree/main/test/Test_meme.gif">


### Install Package for Udacity Workspace Environment
```
pip install python-docx
sudo apt-get install poppler-utils
```

### Install Package for Local Machine 
```
pip install -r requirements.txt
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
│   ├── SimpleLines/
│   └── photos/dog/
│
├── app.py 
├── meme.py                      # Main application script
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```
