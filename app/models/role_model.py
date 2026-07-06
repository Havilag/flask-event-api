from sqlalchemy import Integer, String, Text, DECIMAL, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import db


class Role(db.Model):
    __tablename__ = 'roles'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    
    def to_json(self):
        return{
            'id':self.id,
            'name': self.name
        }