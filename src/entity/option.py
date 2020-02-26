from datetime import datetime

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship

from common.entity_base import BaseEntity, Base


class Option(BaseEntity, Base):
    __tablename__ = 'option'

    id = Column(Integer, primary_key=True)
    description = Column(String(100), nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))

    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    updated_date = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
