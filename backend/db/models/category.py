from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class Category(Base):
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, unique= True, nullable=False)
    products = relationship("Product", back_populates="category")