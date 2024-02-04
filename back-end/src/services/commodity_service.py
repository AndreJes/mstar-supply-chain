from database.database import db_session
from models import Commodity as model

class CommodityService():
    
    def get(self, id:int) -> model:
        return model.query.filter(model.ID_==id).first()

    def list_all(self) -> list[model]:
        return model.query.all()
    
    def insert(self, entity:model) -> None:
        result = db_session.add(entity)
        db_session.commit()
        return result

    def update(self, id:int, new_data:dict) -> model:
        entity = self.get(id)

        for key, value in new_data.items():
            setattr(entity, key, value)

        db_session.commit()

        return self.get(entity.ID_)

    def delete(self, id:int) -> None:
        entity = self.get(id)
        db_session.delete(entity)
        db_session.commit()

