from database.database import db_session
from models import CommodityType as model

class CommodityTypeDAO():
    
    def get(self, name:str) -> model:
        return model.query.filter(model.ID_==name).first()

    def list_all(self) -> list[model]:
        return model.query.all()
    
    def insert(self, entity:model) -> None:
        result = db_session.add(entity)
        db_session.commit()
        return result

    def update(self, name:str, new_data:dict) -> model:
        entity = self.get(name)

        for key, value in new_data.items():
            setattr(entity, key, value)

        db_session.commit()

        return self.get(entity.NAME_)

    def delete(self, name:str) -> None:
        entity = self.get(name)
        db_session.delete(entity)
        db_session.commit()

