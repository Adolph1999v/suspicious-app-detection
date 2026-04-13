
# Suspicious App Detection API with Risk Scoring

## 📌 Overview
This project is a Python-based backend API that analyzes mobile applications and detects potentially suspicious behavior based on the permissions they request.

The system evaluates each app and assigns:
- A **risk score (0–10)**
- A **risk level (LOW / MEDIUM / HIGH)**
- A **suspicious flag (true/false)**
- A **human-readable explanation**

---

## 🎯 Problem Statement
Mobile applications often request permissions that may not align with their intended functionality. This system identifies such mismatches and flags potentially suspicious apps.

---

## ⚙️ Tech Stack
- Python
- FastAPI
- Pydantic

---

## 🧠 How It Works

### 1. App Category Detection
The system infers the app type (e.g., calculator, calendar, communication) based on its name using keyword matching.

*Why?*  
Different app types are expected to use different permissions.

---

### 2. Permission Analysis

The system evaluates permissions using three checks:

#### ✅ Expected Permissions
Each app category has a predefined set of expected permissions.

If permissions match expectations → **No risk added**

---

#### ⚠️ Unexpected Permissions
Permissions not typically required for that app type.

Adds moderate risk: +1.5 per unexpected permission

---

#### 🚨 Dangerous Permissions
High-risk permissions such as:
- READ_CONTACTS
- SEND_SMS
- RECORD_AUDIO

Adds high risk: +2 per dangerous permission (only if unexpected)


---

#### Excessive Permissions
Apps requesting too many permissions (>5)

Adds small risk: +1


---

### 3. Risk Classification

| Score | Level |
|------|------|
| 0 – 3 | LOW |
| 4 – 6 | MEDIUM |
| 7 – 10 | HIGH |

---

### 4. Explanation Generation
Each result includes a clear explanation describing why the app was flagged as suspicious.

This improves transparency and usability.

---

## API Endpoint

---

## Request Input Example

<img width="709" height="129" alt="Screenshot 2026-04-13 at 10 30 04 pm" src="https://github.com/user-attachments/assets/0f993711-5ae4-4c78-a8f2-df1e5695099e" />


## Request Output Example

<img width="881" height="182" alt="Screenshot 2026-04-13 at 10 28 40 pm" src="https://github.com/user-attachments/assets/bffa25f7-58c0-436c-9661-f71613cc035a" />

## Design Decisions
- Rule-based scoring for simplicity and explainability  
- Set operations to easily check which permissions are normal and which are unusual
- Only flag apps when they do something unusual or risky, to avoid unnecessary warnings 

## Future Improvements
- Add ML and DL based anomaly detection  
- Use real-world app datasets for better predictions 
- Improve category detection using fuzzy matching or NLP to handle typos and better understand app names
- Add logging, monitoring, and deployment support  
