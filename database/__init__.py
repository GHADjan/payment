from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Подключения к самой базе
SQLALCHEMY_DATABASE_URI = "sqlite:///pay_test.db"
# connect_args={"check_same_thread": False} Только для подключения sqlite3
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)


# Общий класс для создания моделей данных
Base = declarative_base()

# Генерация подключений к базе
def get_db():
    session = SessionLocal()

    try:
        yield session

    except:
        session.rollback()
        raise

    finally:
        session.close()


# Импорт функционала для БД
from database.userservice import *
from database.businesservice import *
from database.cardservice import *
from database.paymentservice import *


