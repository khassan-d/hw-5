from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    cash = {} # Створення кешу для зберігання
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1

        if n not in cash:
            cash[n] = fibonacci(n-1) + fibonacci(n-2) # рекурсивна функція
        return cash[n] # трохи відійшов від псевдокоду на платформі, таким чином скоротивши код на один return :)
    return fibonacci

def main():
    fib = caching_fibonacci()
    print(fib(10), fib(15)) # 55 i 610 відповідно

if __name__ == "__main__":
    main()