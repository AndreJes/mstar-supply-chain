import os
from urllib.parse import quote  

def get_database_connection_string(*, engine:str="mysql", schema="mstar_supplychain", charset="utf8mb4") -> str:
    database_host = os.environ["DATABASE_HOST"]    
    database_port = os.environ["DATABASE_PORT"]    
    database_user = os.environ["DATABASE_USER"]    
    database_password = os.environ["DATABASE_PASSWORD"]

    # return example: mysql://xxxx:1234@127.0.0.1:3306/mstar_supplychain
    return f"{engine}://{database_user}:{quote(database_password)}@{database_host}:{database_port}/{schema}?charset={charset}"