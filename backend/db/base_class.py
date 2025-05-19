from typing import Any
import re
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative
from sqlalchemy import MetaData
@as_declarative()
class Base:
    id: Any
    __name__: str
    metadata = MetaData()
    #to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()
        return name