# PDF Summary Application

This project is a web application built using Python and Gradio that allows users to upload PDF files and receive a summarized version of their content. The application utilizes Together AI for summarization.

## Project Structure

```
pdf-summary-app
├── src
│   ├── app.py              # Main entry point of the Gradio web application
│   ├── utils
│   │   ├── pdf_reader.py   # Functions for reading PDF files
│   │   └── summarizer.py    # Functions for summarizing text using Together AI
├── requirements.txt         # Project dependencies
├── README.md                # Documentation for the project
├── .gitignore               # Files and directories to ignore by Git
└── runtime.txt              # Python version for Hugging Face Spaces
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd pdf-summary-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python src/app.py
   ```

## Usage

- Open the web application in your browser.
- Upload a PDF file using the provided interface.
- Click on the "Summarize" button to receive a summary of the PDF content.

## Notes

- Ensure that you have access to Together AI's API for summarization.
- The application is designed to be hosted on Hugging Face Spaces for easy access and sharing.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.