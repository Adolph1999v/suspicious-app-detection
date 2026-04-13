# Importing the required libraries
from fastapi import FastAPI                          # FastAPI for API
from pydantic import BaseModel,field_validator       # Used to validate input data
from typing import List                              # Helps define list types

# Initializing the API app
app = FastAPI()  


# Input Data Models
class AppInput(BaseModel):
    name: str                     # App name (string)
    permissions: List[str]        # List of permissions (list of strings)

      # Validate name - returns an error when the app name is empty
    @field_validator("name")
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("App name and/or the Permissions List cannot be empty")
        return value

    # Validate permissions list - rturns an error when the permissions list is empty
    @field_validator("permissions")
    def permissions_must_not_be_empty(cls, value):
        if not value:
            raise ValueError("App name and/or the Permissions List cannot be empty")
        return value

class RequestBody(BaseModel):
    apps: List[AppInput]          # List of apps coming in request


# List of Permissions

# Dangerous permissions (high-risk ones)
DANGEROUS_PERMISSIONS = {
    "READ_CONTACTS",
    "WRITE_CONTACTS",
    "ACCESS_FINE_LOCATION",
    "ACCESS_COARSE_LOCATION",
    "READ_SMS",
    "SEND_SMS",
    "RECORD_AUDIO",
    "CAMERA",
    "READ_CALL_LOG",
    "WRITE_CALL_LOG",
    "READ_EXTERNAL_STORAGE",
    "WRITE_EXTERNAL_STORAGE"
}

# Expected permissions based on app category
EXPECTED_PERMISSIONS = {
    "calculator": set(),  # Calculator should not need permissions
    "calendar": {"READ_CALENDAR", "WRITE_CALENDAR"},
    "camera": {"CAMERA", "WRITE_EXTERNAL_STORAGE"},
    "communication": {"READ_CONTACTS", "SEND_SMS", "INTERNET"},
    "navigation": {"ACCESS_FINE_LOCATION", "INTERNET"},
    "storage": {"READ_EXTERNAL_STORAGE", "WRITE_EXTERNAL_STORAGE"},
    "general": {"INTERNET"}  # Default assumption
}


#  This function tries to guess what type of app it is based on the app name 
def infer_app_category(app_name: str):
    
    name = app_name.lower()  # Convert to lowercase for easier matching

    if "calculator" in name:
        return "calculator"
    elif "calendar" in name:
        return "calendar"
    elif "camera" in name:
        return "camera"
    elif "chat" in name or "messenger" in name:
        return "communication"
    elif "map" in name or "gps" in name:
        return "navigation"
    elif "file" in name or "storage" in name:
        return "storage"
    else:
        return "general"  # Default category


# RISK CALCULATION - This function calculates the risk score, level, and explanation.
def calculate_risk(app):

    permissions = set(app.permissions)  # Converting list to set for faster operations
    name = app.name                     # Get app name

    # Identify app category
    category = infer_app_category(name)

    # Get expected permissions for that category
    expected = EXPECTED_PERMISSIONS.get(category, set())

    score = 0        
    reasons = []     # Stores the explanation 

    # Check for Dangerous Permissions - Each dangerous permission adds 2 points
    dangerous_used = permissions & DANGEROUS_PERMISSIONS  

    # Only penalize dangerous permissions if they are NOT expected
    dangerous_unexpected = dangerous_used - expected

    score += len(dangerous_unexpected) * 2  

    if dangerous_unexpected:
        reasons.append(
        f"Dangerous Permissions used: {', '.join(dangerous_unexpected)}"
    )

    # Unexpected Permissions - Permissions not expected for this app
    unexpected = permissions - expected  

    # Each unexpected permission adds 1.5 points
    if unexpected:
        score += len(unexpected) * 1.5  
        reasons.append(
            f"Unexpected permissions for {category} app: {', '.join(unexpected)}"
        )

    # Slight penalty for too many permissions
    if len(permissions) > 5:
        score += 1  
        reasons.append("Too many permissions requested")

    # Capping the score to 10
    score = min(score, 10)  

    # Classifying the risk based on risk score
    if score >= 7:
        level = "HIGH"
    elif score >= 4:
        level = "MEDIUM"
    else:
        level = "LOW"

    # Final Output
    return {
        "name": name,
        "risk_score": round(score, 2),
        "risk_level": level,
        "is_suspicious": score >= 4,
        "explanation": " | ".join(reasons) if reasons else "Permissions align with expected functionality"
    }


# Creating the API route - It receives the input, processes each app, and returns results
@app.post("/analyze-apps")
def analyze_apps(data: RequestBody):

    # Process each app using risk function
    results = [calculate_risk(app) for app in data.apps]

    # Return final output
    return {"results": results}