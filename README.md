# ANOMCLIP — Phase 1 Starter

A mobile-first, branded AI reel-clipper frontend and a small FastAPI foundation.

## What works now
- Responsive ANOMCLIP dashboard
- Local video file picker and browser preview
- YouTube URL input (saved as a project input; downloading/processing is not implemented yet)
- Project cards and basic UI interactions
- FastAPI health endpoint and placeholder API routes

## What does NOT work yet
- AI transcription, highlight detection, face tracking, rendering, cloud storage and user accounts.
- YouTube downloading. Add only a lawful, terms-compliant ingestion method for videos you own or are authorized to use.
- This is Phase 1, not a finished clipping service.

## Deploy the frontend free
1. Create a GitHub repository named `anomclip`.
2. Upload the contents of this folder (keep `frontend/`).
3. In GitHub: Settings → Pages → Deploy from a branch → `main` → `/frontend` (or move `frontend` contents to repository root and select `/root`).
4. Wait for the published Pages URL.

GitHub Pages hosts static files only. It cannot run Python, Whisper or FFmpeg.

## Run the backend locally (requires a computer)
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000/health

## Android-only workflow
You can create the GitHub repository and upload files using github.com in Chrome. Use GitHub's web editor or upload the extracted files. You do not need to run Python on your phone to publish the static frontend.

## Next phase
Connect a cloud processing API with durable object storage, authentication, job queue and worker. Do not accept large uploads until storage and limits are configured.
