from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from sqlalchemy.orm import relationship

from database.database import Base

@dataclass
class CommodityInbound(Base):
    __tablename__ = 'commodity_inbound'
    ID_ : int = Column(Integer, primary_key=True, autoincrement=True)
    DATE_ : str = Column(DateTime, nullable=False)
    LOCALE_ : str = Column(String(500), nullable=False)
    AMOUNT_ : int = Column(Integer, nullable=False)

    COMMODITY_ID_ : int  = Column(Integer, ForeignKey("commodity.ID_", onupdate="RESTRICT", ondelete="RESTRICT"), nullable=False)
    COMMODITY = relationship("Commodity", backref="Commodity")

    def __init__(self, date, locale, amount, commodity_id, id=None):
        self.DATE_ = date
        self.LOCALE_ = locale
        self.AMOUNT_ = amount
        self.COMMODITY_ID_ = commodity_id
        
        if not id is None:
            self.ID_ = id

    def __repr__(self):
        return f'<CommodityInbound {self.DATE_!r} | {self.LOCALE_!r} | {self.AMOUNT_!r} | {self.COMMODITY_ID_!r}>'
    
    @staticmethod
    def from_dict(dict_entity):
        return CommodityInbound(dict_entity["DATE_"],
                         dict_entity["LOCALE_"],
                         dict_entity["AMOUNT_"],
                         dict_entity["COMMODITY_ID_"],
                         dict_entity.get("ID_", None))