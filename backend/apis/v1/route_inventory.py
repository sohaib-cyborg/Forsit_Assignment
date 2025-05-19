from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from db.repository.inventory import getInventoryStatus, updateInventoryLevel
from db.schemas.inventory import InventoryResponseData
from db.session import get_db

import logging
router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/api/v1/inventory-status", response_model=InventoryResponseData, status_code=status.HTTP_200_OK)
def getCurrentInventoryStatus(inventory_id:int,db: Session= Depends(get_db)):
    try:
        return getInventoryStatus(inventory_id,db)
    except Exception as e:
        logger.error(f"Error fetching Inventory Status: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.put("/Inventory/{id}", response_model=str)
def updateInventory(id:int, order_level:int, db:Session = Depends(get_db)):
    return updateInventoryLevel(id, order_level, db)
       