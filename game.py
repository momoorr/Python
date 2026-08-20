import random

def play_game():
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("=== 숫자 맞히기 게임 (Up & Down) ===")
    print(f"1부터 100 사이의 숫자를 맞혀보세요! (기회: {max_attempts}번)")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\n[{attempts + 1}/{max_attempts}] 숫자를 입력하세요: "))
        except ValueError:
            print("올바른 정수를 입력해주세요.")
            continue

        if not 1 <= guess <= 100:
            print("1과 100 사이의 숫자만 입력 가능합니다.")
            continue

        attempts += 1

        if guess < target_number:
            print("🔼 UP! 더 큰 숫자입니다.")
        elif guess > target_number:
            print("🔽 DOWN! 더 작은 숫자입니다.")
        else:
            print(f"🎉 정답입니다! {attempts}번 만에 맞히셨네요.")
            break
    else:
        print(f"\n💀 아쉽네요! 기회를 모두 사용했습니다. 정답은 {target_number}였습니다.")

if __name__ == "__main__":
    play_game()