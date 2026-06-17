def clean_text(text):
    if not text:
        return ""
    # Remove excessive whitespace
    return " ".join(text.split())
