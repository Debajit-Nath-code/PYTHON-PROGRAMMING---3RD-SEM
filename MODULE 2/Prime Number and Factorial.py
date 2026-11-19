def check_prime(val):
    if val < 2:
        return False
    if val == 2:
        return True
    if val % 2 == 0:
        return False
    factor = 3
    while factor * factor <= val:
        if val % factor == 0:
            return False
        factor += 2
    return True

def run_app():
    val = int(input("Enter an integer: "))
    if check_prime(val):
        print(f"{val} is a prime number.")
    else:
        print(f"{val} is not a prime number.")

if __name__ == "__main__":
    run_app()
