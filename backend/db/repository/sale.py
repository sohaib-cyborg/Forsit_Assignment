from db.models.sales import Sale
from db.models.product import Product
from db.models.category import Category
from sqlalchemy.orm import Session
from sqlalchemy import func, select, text
from sqlalchemy.orm import Session
from datetime import date

def getDailyResults(db:Session):
    query = (
        select(
            func.to_char(Sale.created_at, 'YYYY-MM-DD').label('day'),
            func.sum(Sale.quantity).label('total_quantity_sold'),
            func.sum(Sale.total_amount).label('total_sales')
        )
        .group_by(func.to_char(Sale.created_at, 'YYYY-MM-DD'))
        .order_by(func.min(Sale.created_at))
    )
    result = db.execute(query)
    return result.all()

def getWeeklyResults(db:Session):
    week_start = (func.date_trunc('week', Sale.created_at) + text("interval '1 day'")).label('week_start')
    week_end = (func.date_trunc('week', Sale.created_at) + text("interval '7 day'")).label('week_end')
    query = (
        select(
            week_start,
            week_end,
            func.sum(Sale.quantity).label('total_quantity_sold'),
            func.sum(Sale.total_amount).label('total_sales')
        )
        .group_by(
          func.date_trunc('week', Sale.created_at))
        .order_by(week_start)
    )
    result = db.execute(query)
    return result.all()

def getMonthlyResults(db:Session):
    month = (func.to_char(Sale.created_at,'YYYY-MM').label("month"))
    query = (
        select(
            month,
            func.sum(Sale.quantity).label('total_quantity_sold'),
            func.sum(Sale.total_amount).label('total_sales')
        )
        .group_by(
          month)
        .order_by(month)
    )
    result = db.execute(query)
    return result.all()

def getYearlyResults(db:Session):
    year = (func.to_char(Sale.created_at,'YYYY').label("year"))
    query = (
        select(
            year,
            func.sum(Sale.quantity).label('total_quantity_sold'),
            func.sum(Sale.total_amount).label('total_sales')
        )
        .group_by(
          year)
        .order_by(year)
    )
    result = db.execute(query)
    return result.all()

def getResultsByProduct(product_id:int, db:Session):
    result=(
        db.query(
        Sale.product_id.label('product_id'),
        Product.product_name.label('product_name'),
        func.sum(Sale.quantity).label('total_quantity_sold'),
        func.sum(Sale.total_amount).label('total_sales'),
        func.avg(Sale.sold_at).label('average_sold_at'),
        func.avg(Sale.discount).label('average_discount'),
    ).join(Sale.product).filter(Product.product_id == product_id)
    .group_by(Sale.product_id, Product.product_name)
        .first()
    )
    return result

def getResultsByCategory(category_id:int, db:Session):
    result=(
        db.query(
        Category.category_id.label('category_id'),
        Category.category_name.label('category_name'),
        func.sum(Sale.quantity).label('total_quantity_sold'),
        func.sum(Sale.total_amount).label('total_sales'),
        func.avg(Sale.sold_at).label('average_sold_at'),
        func.avg(Sale.discount).label('average_discount'),
    ).join(Sale.product).join(Category).filter(Category.category_id == category_id)
    .group_by(Category.category_id, Category.category_name)
        .first()
    )
    return result

def getResultsByDateRange(d1:date, d2:date, db:Session):
    result = (
        db.query(
        func.sum(Sale.quantity).label('total_quantity_sold'),
        func.sum(Sale.total_amount).label('total_sales'),
        func.avg(Sale.sold_at).label('average_sold_at'),
        func.avg(Sale.discount).label('average_discount'),        
    ).filter((Sale.created_at >= d1) & (Sale.created_at <= d2))
    .first()
    )
    return result

def getRevenueComparisonByCategory(category_id_1: int, category_id_2: int, db: Session):
    results = (
        db.query(
            Category.category_id.label('category_id'),
            Category.category_name.label('category_name'),
            func.sum(Sale.quantity).label('total_quantity_sold'),
            func.sum(Sale.total_amount).label('total_sales')
        )
        .join(Product, Product.category_id == Category.category_id)
        .join(Sale, Sale.product_id == Product.product_id)
        .filter(Category.category_id.in_([category_id_1, category_id_2]))
        .group_by(Category.category_id, Category.category_name)
        .all()
    )


   
    quantity_diff = abs(results[0].total_quantity_sold - results[1].total_quantity_sold)
    sales_diff = abs(results[0].total_sales - results[1].total_sales)
    return {
        "results": results,
        "difference": {
            "quantity_diff": int(quantity_diff),
            "sales_diff": float(sales_diff)
        }
    }
    
