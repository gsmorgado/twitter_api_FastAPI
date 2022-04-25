# Python
import uvicorn #Server where the app runs
# FastAPI
from fastapi import FastAPI
from routes.user import user

app = FastAPI()
app.include_router(user,prefix="/users", tags=["User"])

# Start server
if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)