from dataclasses import dataclass

from sqlalchemy import Column, String
from database.database import Base

@dataclass
class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    CPF_CNPJ_ : str = Column(String(14), primary_key=True)
    NAME_ : str = Column(String(256), nullable=False)
    DESCRIPTION_ : str = Column(String(1000))
    ADDRESS_ : str= Column(String(512), nullable=False)

    def __init__(self, cpf_cnpj, name, address, *, description=None):
        self.CPF_CNPJ_ = cpf_cnpj
        self.NAME_ = name
        self.DESCRIPTION_ = description
        self.ADDRESS_ = address

    def __repr__(self):
        return f'<Manufacturer {self.CPF_CNPJ_!r} | {self.NAME_!r} | {self.DESCRIPTION_!r}> | {self.ADDRESS_!r}'
    
    @staticmethod
    def from_dict(dict_entity):
        return Manufacturer(dict_entity["CPF_CNPJ_"],
                         dict_entity["NAME_"],
                         dict_entity["ADDRESS_"],
                         description=dict_entity.get("DESCRIPTION_", None))