import random

LOW_LIMIT = 1
HIGH_LIMIT = 10
TOTAL_TRIES = 5

def check_attempt(user_pick, target_val):
    if user_pick < target_val:
        return "low"
    if user_pick > target_val:
        return "high"
    return "correct"

def get_user_pick():
    while True:
        try:
            user_pick = int(input(f"Enter your guess ({LOW_LIMIT}-{HIGH_LIMIT}): "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if LOW_LIMIT <= user_pick <= HIGH_LIMIT:
            return user_pick
        print(f"Please enter a number between {LOW_LIMIT} and {HIGH_LIMIT}.")

def start_round(target_val=None):
    if target_val is None:
        target_val = random.randint(LOW_LIMIT, HIGH_LIMIT)
    elif not LOW_LIMIT <= target_val <= HIGH_LIMIT:
        raise ValueError("Secret number is outside the allowed range.")

    print("========== NUMBER GUESSING GAME ==========")
    print(f"Guess the number between {LOW_LIMIT} and {HIGH_LIMIT}. You have {TOTAL_TRIES} attempts.")

    for turn in range(1, TOTAL_TRIES + 1):
        user_pick = get_user_pick()
        status = check_attempt(user_pick, target_val)
        if status == "correct":
            print(f"Correct! You guessed the number in {turn} attempt(s).")
            return True
        hint = "low" if status == "low" else "high"
        tries_left = TOTAL_TRIES - turn
        print(f"Too {hint}. Attempts remaining: {tries_left}")

    print(f"Game over! The number was {target_val}.")
    return False

if __name__ == "__main__":
    start_round()
