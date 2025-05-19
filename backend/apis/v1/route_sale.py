from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from db.schemas.sale import RevenueComparisonResponse,AggregatedDataByDay, AggregatedDataByWeek, AggregatedDataByMonth, AggregatedDataByYear, saleDataByProduct, saleDataByCategory,  saleDataByDateRange
from db.session import get_db
from db.repository.sale import getRevenueComparisonByCategory,getDailyResults, getWeeklyResults,getMonthlyResults, getYearlyResults, getResultsByProduct, getResultsByCategory, getResultsByDateRange
from typing import List
from datetime import date
import logging
router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/api/v1/daily-sale", response_model=List[AggregatedDataByDay], status_code=status.HTTP_200_OK)
def getDailyRevenue(db: Session= Depends(get_db)):
    try:
        return getDailyResults(db)
    except Exception as e:
        logger.error(f"Error fetching daily sales: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.get("/api/v1/weekly-sale", response_model=List[AggregatedDataByWeek], status_code=status.HTTP_200_OK)
def getWeeklyRevenue(db: Session= Depends(get_db)):
    try:
        return getWeeklyResults(db)
    except Exception as e:
        logger.error(f"Error fetching daily sales: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    
@router.get("/api/v1/monthly-sale", response_model=List[AggregatedDataByMonth], status_code=status.HTTP_200_OK)
def getMonthlyRevenue(db: Session= Depends(get_db)):
    try:
        return getMonthlyResults(db)
    except Exception as e:
        logger.error(f"Error fetching daily sales: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    
@router.get("/api/v1/yearly-sale", response_model=List[AggregatedDataByYear], status_code=status.HTTP_200_OK)
def getYearlyRevenue(db: Session= Depends(get_db)):
    try:
        return getYearlyResults(db)
    except Exception as e:
        logger.error(f"Error fetching daily sales: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    
@router.get("/api/v1/product-sale/{product_id}", response_model=saleDataByProduct, status_code=status.HTTP_200_OK)
def getSaleDataByProduct(product_id:int,db: Session= Depends(get_db)):
    try:
        return getResultsByProduct(product_id,db)
    except Exception as e:
        logger.error(f"Error fetching sales by product: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.get("/api/v1/category-sale/{category_id}", response_model=saleDataByCategory, status_code=status.HTTP_200_OK)
def getSaleDataByCategory(category_id:int,db: Session= Depends(get_db)):
    try:
        return getResultsByCategory(category_id,db)
    except Exception as e:
        logger.error(f"Error fetching sales by Category: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.get("/api/v1/date-range-sale", response_model=saleDataByDateRange, status_code=status.HTTP_200_OK)
def getSaleDataByDateRange(start:date, end:date,db: Session= Depends(get_db)):
    if(end<=start):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="End date (d2) must be greater than start date (d1)."
        )
    try:
        return getResultsByDateRange(start, end,db)
    except Exception as e:
        logger.error(f"Error fetching sales by Date Range: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.get("/api/v1/category-sale/{category_id_1}/{category_id_2}", response_model=RevenueComparisonResponse, status_code=status.HTTP_200_OK)
def getRevenueComparisionDataByCategory(category_id_1:int,category_id_2:int,db: Session= Depends(get_db)):
    try:
        print(getRevenueComparisonByCategory(category_id_1,category_id_2,db))
        return getRevenueComparisonByCategory(category_id_1,category_id_2,db)
    except Exception as e:
        logger.error(f"Error fetching revenue difference by Category: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
