import sys
from pathlib import Path
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    components = line.split(maxsplit=3) # По перших трьох пробілах ділю, а всі інші слова після - в message
    return {
        "date": components[0],
        "time": components[1],
        "level": components[2].lower(), # lower потрібен тут для уникнення повторень нижче
        "message": components[3]
    }

def load_logs(file_path: str) -> list:
    fp = Path(file_path)
    if not fp.exists() or not fp.is_file():
        return []

    try: # випадок, коли файл є, але все одно трапиться якась помилка з відкриттям...
        with open(fp, "r", encoding="utf-8") as file_opened:
            return [parse_log_line(line.strip()) for line in file_opened.readlines() if line.strip()]
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level.lower(), logs)) #використовую анонімну функцію для повернення списку тих словників, які мають в значенні левел, що переданий у функцію

def count_logs_by_level(logs: list) -> dict:
    total = defaultdict(int) # використовую дефолтдікт для лаконічності коду. Для підрахунку делотне значення має бути 0, тому тип int
    for log in logs:
        total[log["level"]] += 1 # ключем total стає значення кожного словника, що лежить у списку. Підраховую к-сть
    return total

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    print(f"INFO             | {counts['info']}")
    print(f"DEBUG            | {counts['debug']}")
    print(f"ERROR            | {counts['error']}")
    print(f"WARNING          | {counts['warning']}")

def main():
    if len(sys.argv) > 3 or len(sys.argv) < 2: # Перевірка чи не забагато аргументів та чи введені вони взагалі
        print("Скрипт приймає лише шлях до файлу логів та, опціонально, рівень логування!")
        return # Я не знаю як завершувати програму без сліду в консолі. Але це наче працює. Не знаю правда чи таке практикують... скажіть будь ласка

    logs_base = load_logs(sys.argv[1]) # Перевірка на валідність адреси файлу відбувається у самому методі
    if not logs_base:  # випадок, коли load_logs поверне []
        print("Немає логів для обробки.")
        return

    counted_logs_lvls = count_logs_by_level(logs_base)
    display_log_counts(counted_logs_lvls) # дефолтний вивід скрипту

    if len(sys.argv) == 3: # додатковий вивід у випадку наявності другого аргументу
        if sys.argv[2].lower() not in ['info', 'debug', 'error', 'warning']:
            print("Такий рівень логування не існує у файлі. Спробуйте: info, debug, error або warning.")
            return

        filtered = filter_logs_by_level(logs_base, sys.argv[2])
        print(f"Деталі логів для рівня '{sys.argv[2].upper()}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()