
---
## How to Run the App Detection API 

This guide will help you run the project even if you are not from a technical background.

---

## Step 1: Install Python

1. Go to: https://www.python.org/downloads/
2. Download and install Python (version 3.9 or higher)
3. During installation, make sure to check:
    "Add Python to PATH"

---

##  Step 2: Install Required Packages

Open Terminal / Command Prompt and run: pip install fastapi uvicorn


---

## Step 3: Create a Project folder and downlaod the main.py file from this GitHub repository

Open the `main.py` in Visual Studio Code or any preferred IDE of your choice

Open terminal within the IDE platform and run the command : uvicorn main:app --reload

You should see something like: Uvicorn running on http://127.0.0.1:8000


---

## 🌐 Step 4: Open the API in Browser

Go to: http://127.0.0.1:8000/docs


This opens a user-friendly interface.

---

## 🧪 Step 7: Test the API

1. Click on **POST /analyze-apps**
2. Click **"Try it out"**
3. Paste this example:

```json
{
  "apps": [
    {
      "name": "Calculator Pro",
      "permissions": ["READ_CONTACTS", "INTERNET"]
    }
  ]
}

Click Execute

