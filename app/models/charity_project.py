from sqlalchemy import Column, String, Text

from app.core.db import BaseCharityDonation


class CharityProject(BaseCharityDonation):
    name = Column(String(110), unique=True, nullable=False)
    description = Column(Text, nullable=False)
