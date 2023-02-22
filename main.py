from api.example import get_nobel_prizes
import asyncio


def main():
    """Entry point for the application"""
    response = asyncio.run(get_nobel_prizes())
    nobel_prize_count = response["meta"]["count"]
    print(
        f"There are a total of {nobel_prize_count} nobel prizes award from 1901 to date, according to nobelprize.org"
    )


if __name__ == "__main__":
    main()
