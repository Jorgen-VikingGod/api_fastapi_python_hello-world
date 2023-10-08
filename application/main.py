import uvicorn
from config import settings
from fastapi import FastAPI

app = FastAPI(
    title="My Super Project",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="1.0.0",)


@app.get("/api/messages/public")
def public():
    return {"text": "This is a public message."}


@app.get("/api/messages/protected")
def protected():
    return {"text": "This is a protected message."}


@app.get("/api/messages/admin")
def admin():
    return {"text": "This is an admin message."}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.port,
        reload=settings.reload,
        server_header=False,
    )
