import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r"\s\d+[.]\d+\s" # патерн для пошуку чисел що розділені точкою (дійсних чисел, таких як у прикладі)
    numbers = re.findall(pattern, text) # у намберс повертаю список співпадінь
    for number in numbers: # ітеруюся по кожному елементу в списку
        yield number

def sum_profit(text: str, func: Callable):
    total = 0
    for num in func(text):
        total += float(num) # так як re.findall повертав куски рядків, перетворюю їх у тип float перед додаванням
    return total

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}") # як і очікувано, виводить 1351.46

if __name__ == "__main__":
    main()