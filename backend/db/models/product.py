from sqlalchemy import DECIMAL,Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from db.base_class import Base


class Product(Base):
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, unique= True, nullable=False)
    product_description = Column(String, nullable=False)
    price = Column(DECIMAL, nullable=False)
    category_id = Column(Integer, ForeignKey("category.category_id"), nullable=False)
    manufacturer_id = Column(Integer, ForeignKey("manufacturer.manufacturer_id"), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)  
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    category = relationship("Category", back_populates="products")
    inventories = relationship("Inventory", back_populates="product")  
    sales = relationship("Sale", back_populates="product")          
    manufacturer = relationship("Manufacturer", back_populates="products")