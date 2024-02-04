from dataclasses import dataclass

from sqlalchemy import Column, String
from database.database import Base

@dataclass
class CommodityType(Base):
    __tablename__ = 'commodity_type'
    NAME_ : str = Column(String(50), primary_key=True)
    DESCRIPTION_ : str = Column(String(500))

    def __init__(self, name, description=None):
        self.NAME_ = name
        self.DESCRIPTION_ = description

    def __repr__(self):
        return f'<CommodityType {self.NAME_!r} | {self.DESCRIPTION_!r}>'
    
    @staticmethod
    def from_dict(dict_entity):
        return CommodityType(dict_entity["NAME_"],
                             dict_entity.get("DESCRIPTION_", None))