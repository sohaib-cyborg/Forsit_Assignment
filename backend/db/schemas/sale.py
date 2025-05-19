from pydantic import BaseModel
from datetime import datetime
from typing import List
class AveragedData:
    average_discount: float|None
    average_sold_at: float|None

class AggregatedData(BaseModel):
    total_quantity_sold: int|None
    total_sales: float|None

class AggregatedDataByDay(AggregatedData):
    day:str
    class Config():
        orm_mode = True

class AggregatedDataByWeek(AggregatedData):
    week_start: datetime
    week_end: datetime
    class Config():
        orm_mode = True      
class AggregatedDataByMonth(AggregatedData):
    month:str
    class Config():
        orm_mode = True   
class AggregatedDataByYear(AggregatedData):
    year:str
    class Config():
        orm_mode = True

class saleDataByProduct(AggregatedData, AveragedData):
    product_id: int
    product_name: str
    class Config():
        orm_mode = True

class saleDataByCategory(AggregatedData, AveragedData):
    category_id: int
    category_name: str
    class Config():
        orm_mode = True

   

class saleDataByDateRange(AggregatedData,AveragedData):
    class Config():
        orm_mode = True

class categoryData(AggregatedData):
    category_id:int
    category_name:str
    class Config():
        orm_mode = True 
class RevenueDifference(BaseModel):
    quantity_diff: int
    sales_diff: float

class RevenueComparisonResponse(BaseModel):
    results: List[categoryData]
    difference: RevenueDifference

                  

