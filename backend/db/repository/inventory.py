from db.models.product import Product
from db.models.inventory import Inventory
from db.models.warehouse import Warehouse
from sqlalchemy.orm import Session
from sqlalchemy import case
from sqlalchemy.orm import Session

def getInventoryStatus(inventory_id:int,db:Session):
    result = (
        db.query(
            Inventory.inventory_id.label('inventory_id'),
            Warehouse.warehouse_name.label('warehouse_name'),
            Product.product_name.label('product_name'),
            Inventory.quantity.label('quantity'),
            Inventory.restock_level.label('restock_level'),
            case(
                (Inventory.quantity < Inventory.restock_level, True),
                else_=False
            ).label('is_restock_needed')
        ).join(Inventory.product).join(Inventory.warehouse).filter(Inventory.inventory_id == inventory_id).first()
    )
    return result

def updateInventoryLevel(inventory_id:int, order_level:int,db: Session):
    if(order_level<=0):
        return "number should be positive"
    inventory = db.query(Inventory).filter(Inventory.inventory_id == inventory_id).first()
    if not inventory:
        return "no such inventory item found"
    inventory.quantity = inventory.quantity + order_level 
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return f"Inventory Updated: New Stock level for Inventory {inventory_id} is {inventory.quantity}"