from gradio import Interface, File, Textbox
from utils.pdf_reader import read_pdf
from utils.summarizer import summarize_text

def summarize_pdf(file):
    text = read_pdf(file.name)
    summary = summarize_text(text)
    return summary

iface = Interface(
    fn=summarize_pdf,
    inputs=File(label="Upload PDF"),
    outputs=Textbox(label="Summary"),
    title="PDF Summary App",
    description="Upload a PDF file to get a summarized version of its content."
)

if __name__ == "__main__":
    iface.launch()