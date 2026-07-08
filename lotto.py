import argparse
import random


def generate_lotto_numbers(count: int = 6, max_number: int = 45) -> list[int]:
    """Generate a sorted list of unique lotto numbers."""
    return sorted(random.sample(range(1, max_number + 1), count))


def generate_draw(draw_count: int = 5, bonus: bool = False) -> list[tuple[list[int], int | None]]:
    """Generate five lotto recommendations by default."""
    draws: list[tuple[list[int], int | None]] = []
    for _ in range(draw_count):
        main_numbers = generate_lotto_numbers()
        bonus_number = None
        if bonus:
            remaining = [n for n in range(1, 46) if n not in main_numbers]
            bonus_number = random.choice(remaining)
        draws.append((main_numbers, bonus_number))
    return draws


def print_draws(draws: list[tuple[list[int], int | None]]) -> None:
    """Print the lotto draw results."""
    for index, (numbers, bonus_number) in enumerate(draws, start=1):
        formatted_numbers = ' '.join(f"{n:02d}" for n in numbers)
        print(f"[{index}] 추첨 번호: {formatted_numbers}")
        if bonus_number is not None:
            print(f"    보너스 번호: {bonus_number:02d}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="로또 번호 추첨기")
    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=5,
        help="생성할 추천 번호 세트 수 (기본값: 5)",
    )
    parser.add_argument(
        "-b",
        "--bonus",
        action="store_true",
        help="보너스 번호도 함께 생성합니다",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.count < 1:
        raise SystemExit("추첨 횟수는 1 이상이어야 합니다.")

    draws = generate_draw(draw_count=args.count, bonus=args.bonus)
    print_draws(draws)


if __name__ == "__main__":
    main()
