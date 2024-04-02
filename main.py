from fastapi import FastAPI,UploadFile,File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

# Create an instance of the FastAPI class
app = FastAPI()

# Define allowed origins
origins = [
    "http://127.0.0.1:5501",
    # Add other origins as needed
]

# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)



# Define a route and its handler function
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/upload/")
async def upload_image(file: UploadFile=File(...)):
    contents=await file.read()
    image=Image.open(io.BytesIO(contents))
    image.show()
    return {200,"Image received"}
# Run the server with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
