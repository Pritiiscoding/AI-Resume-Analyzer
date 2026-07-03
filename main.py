from backend.parser import extract_text
from backend.extractor import extract_email
from backend.extractor import extract_phone

resume = extract_text("data/resumeofpritipriya.pdf")

print(extract_email(resume))
print(extract_phone(resume))