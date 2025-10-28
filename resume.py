import json, re
from PyPDF2 import PdfReader

pdf_path = r"C:\Users\HP\Desktop\Ask Zyla\Ai resume analyzer\CHANDRU RESUME (1).pdf"
skills_path = r"C:\Users\HP\Desktop\Ask Zyla\Ai resume analyzer\skills.json"


def extract_text(pdf):
    text = ""
    for p in PdfReader(pdf).pages:
        text += p.extract_text() or ""
    return text.lower()

def analyze(text, skills):
    matched, missing = [], []
    for s in skills:
        names = [s["name"].lower()] + [a.lower() for a in s.get("aliases", [])]
        if any(re.search(rf'\b{re.escape(n)}\b', text) for n in names):
            matched.append(s["name"])
        else:
            missing.append(s["name"])
    cov = round(len(matched) / len(skills) * 100, 1)
    return cov, matched, missing

def summary(matched):
    if any(x.lower() in ("django","flask","node","backend") for x in matched):
        part1 = "strong in backend"
    else:
        part1 = "a generalist"
    if any(x.lower() in ("ml","machine learning","ai","pytorch","tensorflow") for x in matched):
        part2 = "and moderate in AI/ML"
    else:
        part2 = ""
    return f"This candidate is {part1} {part2}.".strip()

text = extract_text(pdf_path)
skills = json.load(open(skills_path))
cov, match, miss = analyze(text, skills)

print(f"\nSkill Coverage: {cov}%")
print(f"Matched Skills: {match}")
print(f"Missing Skills: {miss}")
print("AI Summary:", summary(match))
input("\nPress Enter to exit...")



