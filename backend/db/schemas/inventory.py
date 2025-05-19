from pydantic import BaseModel
from datetime import datetime
from typing import List

class InventoryResponseData(BaseModel):
    inventory_id:int
    product_name:str
    warehouse_name:str
    quantity:int
    restock_level:int
    is_restock_needed:bool
    class Config():
        orm_mode = True
class UpdateReorderLevel(BaseModel):
    new_order:int      