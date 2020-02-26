from datetime import datetime

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship

from common.entity_base import Base, BaseEntity
from entity.option import Option


class Question(Base, BaseEntity):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)

    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    updated_date = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    options = relationship("Option", backref="question", lazy='joined')
