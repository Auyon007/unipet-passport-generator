# 🛂 Passport Number Overlay Tool

This Streamlit app allows you to upload a passport image and overlay a dynamically generated or custom passport number at a specified position and font size. Useful for software testing or automation scenarios where unique passport numbers are required.

---

## 🚀 Features

- Upload a passport image (`.jpg`, `.jpeg`, `.png`)
- Auto-generate a random passport number (starts with `TB` + 6 digits)
- Manually enter a passport number if preferred
- Set position (X, Y) and font size manually
- Live preview of modified image

---

## 🧰 Requirements

- Python 3.7+
- Streamlit
- Pillow

Install dependencies:

```bash
pip install -r requirements.txt


How to Run Locally
streamlit run app.py
Then open the browser at http://localhost:8501.
