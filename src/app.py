"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Learn2Earn training Centre.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Learn2Earn Training Centre API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@learn2earn.com", "daniel@learn2earn.com"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@learn2earn.com", "sophia@learn2earn.com"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@learn2earn.com", "olivia@learn2earn.com"]
    }
}

# Additional activities
activities.update({
    "Basketball Club": {
        "description": "Team-based basketball training and friendly matches",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["alex@learn2earn.com"]
    },
    "Swimming Club": {
        "description": "Swimming lessons and lap practice at the community pool",
        "schedule": "Tuesdays and Saturdays, 5:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["lily@learn2earn.com"]
    },
    "Art Club": {
        "description": "Explore drawing, painting, and mixed media projects",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["noah@learn2earn.com"]
    },
    "Music Ensemble": {
        "description": "Group rehearsals for instrumental and vocal performances",
        "schedule": "Fridays, 4:00 PM - 6:00 PM",
        "max_participants": 25,
        "participants": ["ava@learn2earn.com"]
    },
    "Debate Club": {
        "description": "Practice public speaking, argumentation, and competitive debates",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["liam@learn2earn.com"]
    },
    "Science Club": {
        "description": "Hands-on experiments, science fairs, and research projects",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["mia@learn2earn.com"]
    }
})


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
