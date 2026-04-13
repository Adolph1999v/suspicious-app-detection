
# How to Run the App Detection API

This guide explains how to set up and run the Suspicious App Detection API on your local machine.

---

## Step 1: Install Python

1. Go to: https://www.python.org/downloads/
2. Download and install Python (version 3.9 or higher)
3. During installation, make sure to check:
   **"Add Python to PATH"**

---

## Step 2: Install Required Packages

Open Terminal (Mac/Linux) or Command Prompt (Windows) and run:

```bash
pip install fastapi uvicorn pydantic
```

### Package Details

* **fastapi** → Backend framework used to build the API
* **uvicorn** → ASGI server used to run the application
* **pydantic** → Data validation and request parsing


---

## Step 3: Set Up the Project

1. Create a new project folder
2. Download the `main.py` file from this repository
3. Open the folder in Visual Studio Code (or any IDE)

---

## Step 4: Run the Server

Open the terminal inside your IDE and run the command:

```bash
uvicorn main:app --reload
```

You should see output similar to:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## Step 5: Open the API Interface

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

This will open FastAPI’s interactive API documentation, where you can test the endpoints.

---

## Step 6: Test the API

1. Locate **POST /analyze-apps**
2. Click **"Try it out"**
3. Paste the example request below:

```json
{
  "apps": [
    {
      "name": "Calculator Pro",
      "permissions": ["READ_CONTACTS", "INTERNET"]
    }
  ]
}
```

4. Click **Execute**

You will receive a response containing the risk score, level, and explanation for the app.

---


