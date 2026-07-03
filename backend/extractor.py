import re
def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    emails = re.findall(pattern, text)

    return emails

def extract_phone(text):
    phones = re.findall(r"\d{10}", text)

    return phones

def extract_linkedin(text):
    pattern = r"https?://(?:www\.)?linkedin\.com/\S+"

    return re.findall(pattern, text)

def extract_github(text):
    github = r"https?://(?:www\.)?github\.com/\S+"

