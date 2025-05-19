from fastapi import APIRouter

from apis.v1 import route_sale,route_inventory


api_router = APIRouter()
api_router.include_router(route_sale.router,prefix="",tags=["sale"])

api_router.include_router(route_inventory.router,prefix="",tags=["inventory"])