"""
# перше завдання 
from datetime import datetime

def get_days_from_today(date):
    try:
        today = datetime.today()
        input_date = datetime.strptime(date, "%Y-%m-%d")
        difference = (today.toordinal() - input_date.toordinal())
        return difference
    except ValueError:
        print("Невірний формат дати. Використовуйте формат YYYY-MM-DD.")
    except TypeError:
        print("Невірний тип даних. Передайте дату у вигляді рядка.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

print(get_days_from_today("2021-10-09"))
"""


"""
# друге завдання
import random
def get_numbers_ticket(min, max, quantity):
    if 1 <= min <= max <= 1000 and 1 <= quantity <= (max - min + 1):
        list_of_num = random.sample(range(min, max + 1), quantity)
        list_of_num.sort()
        return list_of_num
    else:
        print("Мінімальне можливе число у наборі має бути не менше 1, а максимальне можливе число у наборі - не більше 1000.")
        return []

print(get_numbers_ticket(2, -5, 7))
"""


"""
# третє завдання
import re
def normalize_phone(phone_number: str) -> str:
    pattern = r"[^\d+]"
    phone_number = re.sub(pattern, "", phone_number)
    if not phone_number.startswith("+"):
        if phone_number.startswith("380"):
            phone_number = "+" +  phone_number
        else:
            phone_number = "+380" +  phone_number
    return phone_number

print(normalize_phone("38067-123 4567"))
print(normalize_phone("067123 4(567)"))
print(normalize_phone("+46067123 4(567)"))
"""