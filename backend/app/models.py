"""SQLAlchemy models for the application."""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base


# Placeholder for future models
# Example model structure:
# class ExampleModel(Base):
#     __tablename__ = "examples"
#     
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
