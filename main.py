from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl

app = FastAPI(title="ANOMCLIP API", version="0.1.0")

# Replace the wildcard with your deployed frontend origin before production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class ProjectInput(BaseModel):
    source_url: HttpUrl

@app.get("/health")
def health():
    return {"app": "ANOMCLIP", "phase": 1, "status": "online"}

@app.post("/api/projects")
def create_project(project: ProjectInput):
    # Phase 1 placeholder: no downloading or video processing occurs here.
    return {
        "status": "received",
        "source_url": str(project.source_url),
        "message": "Project API foundation ready. Processing engine is not connected yet."
    }
