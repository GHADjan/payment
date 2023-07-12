from database.models import Transaction, ServiceCategory, Service
from database import get_db


# Регистрация категории бизнеса
def register_business_category_db(category_name: str):
    db = next(get_db())
    new_category = ServiceCategory(category_name=category_name)
    db.add(new_category)
    db.commit()

    return "Категория бизнеса успешно зарегистрирована"


# Регистрация бизнеса
def register_business_db(category_id: int, name: str, card_number: int):
    db = next(get_db())
    new_business = Service(service_categories=category_id,
                           service_name=name,
                           service_check=card_number)
    db.add(new_business)
    db.commit()

    return "Бизнес успешно зарегистрирован"


# Вывод всех категорий
def get_business_categories_db(exact_category_id: int = 0):
    db = next(get_db())
    if exact_category_id == 0:
        categories = db.query(ServiceCategory).all()
    else:
        categories = db.query(ServiceCategory).filter_by(category_name=exact_category_id).all()

    return categories


# Вывод услуг
def get_exact_business_db(business_id: int, service_categories: int):
    db = next(get_db())
    business = db.query(Service).filter_by(service_id=business_id,
                                           service_categories=service_categories).first()

    if business:
        return business
    else:
        return "Бизнес не найден"


# Оплата услуги
def pay_for_service_db(business_id: int, from_card: int, amount: float):
    db = next(get_db())
    transaction = Transaction(business_id=business_id,
                              card_id=from_card,
                              amount=amount)
    db.add(transaction)
    db.commit()

    return "Услуга успешно оплачена"


# Удалить бизнес
def delete_business_db(business_id: int):
    db = next(get_db())
    business = db.query(Service).filter_by(service_id=business_id).first()

    if business:
        db.delete(business)
        db.commit()
        return "Бизнес успешно удален"
    else:
        return "Бизнес не найден"


# Удалить категорию
def delete_business_category_db(category_id: int):
    db = next(get_db())
    category = db.query(Service).filter_by(service_id=category_id).first()

    if category:
        db.delete(category)
        db.commit()
        return "Бизнес категория успешно удален"
    else:
        return "Бизнес категория не найден"

