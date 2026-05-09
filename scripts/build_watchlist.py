import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.watchlist import get_default_watchlist, save_watchlist


def main() -> None:
    watchlist = get_default_watchlist()
    save_watchlist(watchlist, path="data/watchlist.json")
    print(f"Saved watchlist with {len(watchlist)} tickers:")
    print(", ".join(watchlist))


if __name__ == "__main__":
    main()
