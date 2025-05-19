from sqlalchemy import Column, Integer, DateTime, ForeignKey, func, DECIMAL, Index
from sqlalchemy.orm import relationship

from db.base_class import Base

class Sale(Base):
    sales_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.product_id"), nullable=False)
    warehouse_id = Column(Integer, ForeignKey("warehouse.warehouse_id"), nullable=False)
    manufacturer_id = Column(Integer, ForeignKey("manufacturer.manufacturer_id"), nullable= False)
    total_amount = Column(DECIMAL, nullable=False)
    sold_at = Column(DECIMAL,nullable=False)
    quantity = Column(DECIMAL, nullable=False)
    discount = Column(DECIMAL, nullable= False, default= 0.00)
    created_at = Column(DateTime, default=func.now(), nullable=False, index= True)  
    product = relationship("Product", back_populates="sales")
    warehouse = relationship("Warehouse", back_populates="sales")
    manufacturer = relationship("Manufacturer",back_populates="sales")
    __table_args__ = (
        Index("iix_warehouse_product", "warehouse_id", "product_id", "manufacturer_id"),
    )