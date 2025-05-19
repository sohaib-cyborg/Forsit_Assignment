from sqlalchemy import Column, Integer, DateTime, ForeignKey, func, Index, UniqueConstraint
from sqlalchemy.orm import relationship

from db.base_class import Base

class Inventory(Base):   
    inventory_id = Column(Integer, primary_key=True)
    warehouse_id = Column(Integer, ForeignKey("warehouse.warehouse_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    restock_level = Column(Integer, nullable= False)
    created_at = Column(DateTime, default=func.now(), nullable=False)  
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    warehouse = relationship("Warehouse", back_populates="inventories")
    product = relationship("Product", back_populates="inventories")
    __table_args__ = (
        Index("ix_warehouse_product", "warehouse_id", "product_id"),
        UniqueConstraint('product_id', 'warehouse_id', name='unique_product_warehouse'),
    )
    