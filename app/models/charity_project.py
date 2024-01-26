from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text

from app.core.db import Base


class CharityProject(Base):
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    name = Column(String(110), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    close_date = Column(DateTime, default=None)
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
