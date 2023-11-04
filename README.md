meme-generator/
│
├── app.py                  # The Flask application.
├── meme.py                 # The script to generate memes from the command line.
│
├── QuoteEngine/            # The module for ingesting quotes from various file types.
│   ├── __init__.py
│   ├── QuoteModel.py       # Defines the QuoteModel class.
│   ├── IngestorInterface.py# Abstract base class for ingestors.
│   ├── CSVIngestor.py      # Defines the CSVIngestor class.
│   ├── DocxIngestor.py     # Defines the DocxIngestor class.
│   ├── PDFIngestor.py      # Defines the PDFIngestor class.
│   ├── TextIngestor.py     # Defines the TextIngestor class.
│   └── Ingestor.py         # Defines the Ingestor class that encapsulates all ingestors.
│
├── MemeEngine/             # The module for creating meme images.
│   ├── __init__.py
│   └── MemeEngine.py       # Defines the MemeEngine class.
│
├── static/                 # Directory for static content like images and generated memes.
│   └── ...
│
├── templates/              # Directory for Flask templates.
│   └── ...
│
├── _data/                  # Data directory for sample quotes, images, and fonts.
│   ├── DogQuotes/
│   │   ├── DogQuotesCSV.csv
│   │   ├── DogQuotesDOCX.docx
│   │   ├── DogQuotesPDF.pdf
│   │   └── DogQuotesTXT.txt
│   │
│   ├── Fonts/
│   │   └── LilitaOne-Regular.ttf
│   │
│   └── Photos/
│       └── Dog/
│           └── ...
│
└── requirements.txt        # Python dependencies required for the project.