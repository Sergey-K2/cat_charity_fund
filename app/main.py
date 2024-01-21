from fastapi import FastAPI

from app.core.config import settings
from app.models import CharityProject, Donation, User

app = FastAPI(title=settings.app_title)
