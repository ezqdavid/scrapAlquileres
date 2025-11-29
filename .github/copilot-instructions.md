# Copilot Instructions for scrapAlquileres

## Repository Overview

**scrapAlquileres** is a Python-based OCR project that scrapes and processes rental property listings (alquileres) from newspaper classified ads. It uses Tesseract-OCR to extract text from images and stores the data in a SQLite database.

- **Project Type**: Python OCR/Data Processing application
- **Languages**: Python
- **Key Technologies**: Tesseract-OCR, OpenCV, pandas, SQLite3, Flask
- **Size**: Small (15 lines of Python code in utility modules; main workflow is in a Jupyter notebook)

## Project Structure

```
scrapAlquileres/
├── README.md                    # Project documentation (Spanish)
├── requirements.txt             # Python dependencies
├── scrapClasificados.ipynb     # Main Jupyter notebook with OCR workflow
├── database/
│   └── database.db             # SQLite database file
├── data/
│   ├── import/                 # Input images for OCR processing
│   └── export/                 # Processed output images
└── src/
    ├── __init__.py
    ├── app.py                  # Placeholder for executable application
    └── utils/
        ├── __init__.py
        ├── databaseConnection.py  # SQLite connection helper
        └── sqlQueries.py          # SQL query utilities
```

## Environment Setup

### Prerequisites (System Dependencies)

1. **Python 3.10+** - The project was developed with Python 3.10
2. **Tesseract-OCR** - Required for OCR functionality
   - Linux: `sudo apt-get install tesseract-ocr`
   - Windows: Download from https://digi.bib.uni-mannheim.de/tesseract/

### Python Environment Setup

Always create and activate a virtual environment before installing dependencies:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# Linux/macOS:
source .venv/bin/activate
# Windows CMD:
.venv\Scripts\Activate.bat

# Install setuptools and wheel first (required for building some packages)
pip install --upgrade pip setuptools wheel

# Install dependencies
pip install pandas numpy opencv-python pytesseract Pillow flask selenium
```

**Important Notes**:
- The `requirements.txt` contains some Windows-specific packages (`pywin32`) and unavailable packages (`motoflash2sh`) that will fail on Linux. Install core dependencies explicitly as shown above.
- Always install `setuptools` and `wheel` before other packages to avoid build errors.

## Working with the Codebase

### Key Modules

1. **`src/utils/databaseConnection.py`** - Creates SQLite database connections
   ```python
   from src.utils.databaseConnection import crearConexion
   cursor = crearConexion()  # Returns cursor to database/database.db
   ```

2. **`src/utils/sqlQueries.py`** - SQL query helpers
   ```python
   from src.utils import sqlQueries
   df = sqlQueries.obtenerDfFromQuery(sqlQueries.obtenerAlquileres(), cursor)
   ```

3. **`scrapClasificados.ipynb`** - Main OCR workflow demonstrating:
   - Image loading and preprocessing with OpenCV
   - OCR text extraction with pytesseract
   - Data transformation and storage in SQLite

### Testing Module Imports

```bash
source .venv/bin/activate
python -c "from src.utils.databaseConnection import crearConexion; from src.utils import sqlQueries; print('OK')"
```

### Testing OCR Functionality

```bash
source .venv/bin/activate
python -c "import cv2; import pytesseract; img = cv2.imread('data/import/recorteEjemplo.png'); print('OCR works:', pytesseract.image_to_string(img)[:50])"
```

## Build and Validation

### No CI/CD Pipelines

This repository does not have:
- GitHub Actions workflows
- Linting configuration (.flake8, .pylintrc)
- Test framework setup (pytest, unittest)
- Build scripts (Makefile, setup.py)

### Manual Validation Steps

1. **Verify imports work**:
   ```bash
   python -c "from src.utils.databaseConnection import crearConexion; print('OK')"
   ```

2. **Verify database connection**:
   ```bash
   python -c "from src.utils.databaseConnection import crearConexion; c = crearConexion(); print('DB OK')"
   ```

3. **Verify OCR** (requires tesseract installed):
   ```bash
   python -c "import pytesseract; pytesseract.get_tesseract_version()"
   ```

## Database Schema

The SQLite database (`database/database.db`) contains an `alquileres` table with columns:
- `barrio` - Neighborhood
- `direccion` - Address
- `precio` - Price
- `tipo` - Type
- `caracteristicas` - Features
- `otros` - Other information

## Common Issues and Workarounds

| Issue | Solution |
|-------|----------|
| `motoflash2sh` not found during pip install | Skip it - not required for core functionality |
| `pywin32` fails on Linux | Skip it - Windows-specific package |
| pytesseract cannot find tesseract | Install tesseract-ocr system package |
| Build errors with cffi/MarkupSafe | Install `setuptools wheel` first |

## Guidelines for Code Changes

1. **Spanish context**: Comments and documentation are in Spanish
2. **Database path**: Database is at `database/database.db` - relative to project root
3. **Image paths**: Input images go in `data/import/`, output in `data/export/`
4. **Module imports**: Use `from src.utils...` pattern when importing from project modules
5. **Virtual environment**: Always work within `.venv` - it's in `.gitignore`

Trust these instructions. Only search the codebase if information here is incomplete or found to be incorrect.
