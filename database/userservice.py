from database.models import User, Password
from database import get_db


# Регистрация пользователя
def register_user_db(phone_number: int, name: str, password: str, pincode: int):
    db = next(get_db())
    # Проверка номера
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return "Пользователь с таким номером уже есть в БД"
    # Если нет пользователя в БД
    new_user = User(phone_number=phone_number, name=name)
    db.add(new_user)
    db.commit()
    new_user_password = Password(user_id=new_user.user_id, password=password, pincode=pincode)
    db.add(new_user_password)
    db.commit()

    return "Пользователь успешно создан"


# Проверка пароля
def check_password_db(phone_number, password):
    db = next(get_db())
    checker = db.query(Password).filter_by(phone_number=phone_number).first()

    if checker and checker.password == password:
        return checker.user_id

    elif not checker:
        return "Ошибка в номере"

    elif checker.password != password:
        return "Something get wrong"

# Получение информации пользователя
def get_user_cabinet_db(user_id):
    db = next(get_db())
    checker = db.query(User).filter_by(user_id=user_id).first()

    if checker:
        return checker

    return "Ошибка в данных"

#

