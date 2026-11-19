from functools import lru_cache

TERM_LIMIT = 100

@lru_cache(maxsize=None)
def get_fib(pos):
    if pos < 0:
        raise ValueError("Fibonacci index cannot be negative.")
    if pos <= 1:
        return pos
    return get_fib(pos - 1) + get_fib(pos - 2)

def run_app():
    term_count = int(input("Enter the number of terms: "))
    if term_count <= 0:
        print("Please enter a positive number of terms.")
        return
    if term_count > TERM_LIMIT:
        print(f"Please enter no more than {TERM_LIMIT} terms.")
        return
    sequence = [get_fib(pos) for pos in range(term_count)]
    print("Fibonacci series:")
    print(*sequence)

if __name__ == "__main__":
    run_app()
