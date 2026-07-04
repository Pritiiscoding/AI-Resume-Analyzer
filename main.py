from backend.parser import extract_text
from backend.text_preprocessing import preprocess_text

resume = extract_text("data/sample_resume.pdf")

cleaned_resume = preprocess_text(resume)

print(cleaned_resume)