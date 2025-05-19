from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class Manufacturer(Base):
    manufacturer_id = Column(Integer, primary_key=True)
    manufacturer_name = Column(String, unique= True, nullable=False)
    products = relationship("Product", back_populates="manufacturer")
    sales = relationship("Sale", back_populates="manufacturer")