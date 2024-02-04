from database.database import db_session
from models import Manufacturer as model

class ManufacturerService():
    
    def get(self, cpf_cnpj:str) -> model:
        return model.query.filter(model.cpf_cnpj_==cpf_cnpj).first()

    def list_all(self) -> list[model]:
        return model.query.all()
    
    def insert(self, entity:model) -> None:
        result = db_session.add(entity)
        db_session.commit()
        return result

    def update(self, cpf_cnpj:str, new_data:dict) -> model:
        entity = self.get(cpf_cnpj)

        for key, value in new_data.items():
            setattr(entity, key, value)

        db_session.commit()

        return self.get(entity.CPF_CNPJ_)

    def delete(self, cpf_cnpj:str) -> None:
        entity = self.get(cpf_cnpj)
        db_session.delete(entity)
        db_session.commit()

