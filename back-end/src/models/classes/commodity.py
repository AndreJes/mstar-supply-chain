from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship

from database.database import Base

@dataclass
class Commodity(Base):
    __tablename__ = 'commodity'
    ID_ : int = Column(Integer, primary_key=True, autoincrement=True)
    REGISTRATION_NUMBER_ : str = Column(String(50), unique=True, nullable=False)
    NAME_ : str = Column(String(200), nullable=False)
    DESCRIPTION_ : str = Column(String(1000), nullable=False)
    STOCK_AMOUNT_ : int = Column(Integer, nullable=False)

    MANUFACTURER_RN_ : str  = Column(String(14), ForeignKey("manufacturer.CPF_CNPJ_", onupdate="RESTRICT", ondelete="RESTRICT"), nullable=False)
    MANUFACTURER = relationship("Manufacturer", backref="Commodity")

    TYPE_ : str = Column(String(50), ForeignKey("commodity_type.NAME_", onupdate="RESTRICT", ondelete="RESTRICT"), nullable=False)
    TYPE = relationship("CommodityType", backref="Commodity")

    def __init__(self, registration_number, name, description, manufacturer_rn, type, stock_amount=0, id=None):
        self.REGISTRATION_NUMBER_ = registration_number
        self.NAME_ = name
        self.DESCRIPTION_ = description
        self.MANUFACTURER_RN_ = manufacturer_rn
        self.TYPE_ = type
        self.STOCK_AMOUNT_ = stock_amount
        if not id is None:
            self.ID_ = id

    def __repr__(self):
        return f'<CommodityType {self.REGISTRATION_NUMBER_!r} | {self.NAME_!r} | {self.MANUFACTURER_RN_!r} | {self.TYPE_!r} | {self.STOCK_AMOUNT_!r} | {self.DESCRIPTION_!r}>'
    
    @staticmethod
    def from_dict(dict_entity):
        return Commodity(dict_entity["REGISTRATION_NUMBER_"],
                         dict_entity["NAME_"],
                         dict_entity["DESCRIPTION_"],
                         dict_entity["MANUFACTURER_RN_"],
                         dict_entity["TYPE_"],
                         dict_entity.get("STOCK_AMOUNT_", 0),
                         dict_entity.get("ID_", None))