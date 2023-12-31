from fastapi import FastAPI
from database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


from business import business_api
from card_management_transfer import card_api
from user_authentication import user_api


# Запуск проекта fastapi
# uvicorn main:app --reload

