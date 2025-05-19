from sqlalchemy import Column, Integer, String, Enum as pyNum
from sqlalchemy.orm import relationship
from enum import Enum, unique
from db.base_class import Base

@unique
class Warehouse_Location_Enum(str, Enum): 
    Karachi = "Karachi"
    Seoul = "Seoul"
    Lahore = "Lahore"

class Warehouse(Base):
    warehouse_id = Column(Integer, primary_key=True)
    warehouse_name = Column(String, nullable= False)
    warehouse_location = Column(pyNum(Warehouse_Location_Enum), nullable=False)
    inventories = relationship("Inventory", back_populates="warehouse")
    sales = relationship("Sale", back_populates="warehouse")
