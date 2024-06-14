from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes import bypass  # Import the bypass router

# Load environment variables (optional, depending on your project needs)
load_dotenv()

# Create a FastAPI application instance
app = FastAPI()

# Include the bypass router from the routes module
app.include_router(bypass.router)
