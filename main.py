from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    email = "etwhalay@gmail.com"
    current_time = str(datetime.now().replace(microsecond=0).isoformat())+'Z'
    github_url = "https://github.com/Authvibes/stage-0.git"
    return{
        "email" : email,
        "current_datetime" : current_time,
        "github_url" : github_url
    }