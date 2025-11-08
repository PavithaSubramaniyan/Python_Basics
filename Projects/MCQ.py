import re

# Assume resume file is 'resume.txt' in the same folder
filename = "My Resume.pdf"

# Read the whole file text
with open(filename, "r", encoding="utf-8") as file:
    text = file.read()

# 1. Extract Email (first match)
email = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
email = email[0] if email else "Not found"

# 2. Extract Phone Number (India mobile format)
phone = re.findall(r"\b[789]\d{9}\b", text)
phone = phone[0] if phone else "Not found"

# 3. Extract Name (first non-empty line)
lines = text.split("\n")
name = ""
for line in lines:
    if line.strip() and "resume" not in line.lower() and "curriculum" not in line.lower():
        name = line.strip()
        break
if not name:
    name = "Not found"

# Output results
print("---- Resume Information ----")
print("Name :", name)
print("Email:", email)
print("Phone:", phone)
import re

# Assume resume file is 'resume.txt' in the same folder
filename = "My Resume.pdf"

# Read the whole file text
with open(filename, "r", encoding="utf-8") as file:
    text = file.read()

# 1. Extract Email (first match)
email = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
email = email[0] if email else "Not found"

# 2. Extract Phone Number (India mobile format)
phone = re.findall(r"\b[789]\d{9}\b", text)
phone = phone[0] if phone else "Not found"

# 3. Extract Name (first non-empty line)
lines = text.split("\n")
name = ""
for line in lines:
    if line.strip() and "resume" not in line.lower() and "curriculum" not in line.lower():
        name = line.strip()
        break
if not name:
    name = "Not found"

# Output results
print("---- Resume Information ----")
print("Name :", name)
print("Email:", email)
print("Phone:", phone)
