import re

text = "hello, how are you?"
formatted_text = re.sub(r"([^\w\s])", r"\n\1", text)  # Add newline before special characters
formatted_text = formatted_text.replace(" ", "\n")  # Replace spaces with newlines

print(formatted_text)
