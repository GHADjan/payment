from database.models import Service, Transaction, Card
from database import get_db


# Сделать перевод с карты на карту
def transfer_money_db(card_from, card_to, amount, date):
    db = next(get_db())
    card_from_checker = get_exact_card_balance_db(card_from)
    card_to_checker = get_exact_card_balance_db(card_to)
    if (card_from_checker and card_to_checker) and (card_from_checker.balance >= amount):
        transaction = Transaction(card_to=card_to,
                                  card_id=card_from_checker.card_id,
                                  amount=amount)
        card_from_checker.balance -= amount
        card_to_checker.balance += amount
        db.add(transaction)
        db.commit()
        return "perevod uspewno vipolnen"
    elif not card_to_checker or not card_from_checker:
        return "owibka v dannix"
    else:
        return "nedostatochno sredstv"


def pay_for_service_db(business_id: int, from_card: int, amount: float ):
    db = next(get_db())
    checker = get_exact_card_balance_db(from_card)
    if checker and checker.balance >= amount:
        transaction = Transaction(card_to=business_id,
                                  card_id=from_card,
                                  amount=amount)
        checker.balance -= amount

        db.add(transaction)
        db.commit()
        return "Услуга успешно оплачена"
    elif not checker:
        return "ошибка в данных"
    else:
        return "недостаточно средств"


def get_exact_card_balance_db(card_number):
    db = next(get_db())
    exact_card = db.query(Card).filter_by(card_number=card_number).first()

    return exact_card

