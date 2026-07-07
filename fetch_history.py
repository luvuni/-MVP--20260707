#!/usr/bin/env python3
"""Fetch historical lotto draw data from the official dhLottery endpoint

Usage:
  python fetch_history.py --start 1 --end 1200 --out history.json

If --end is omitted, the script will keep fetching until a failed response is returned.
"""
import argparse
import json
import time
from typing import Dict, List

import requests


def fetch_draw(n: int) -> Dict:
    url = "https://www.dhlottery.co.kr/common.do"
    params = {"method": "getLottoNumber", "drwNo": n}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=0, help="0 = fetch until last available")
    parser.add_argument("--out", default="history.json")
    parser.add_argument("--delay", type=float, default=0.25, help="seconds between requests")
    args = parser.parse_args()

    draws: List[Dict] = []
    n = args.start
    while True:
        try:
            data = fetch_draw(n)
        except Exception as e:
            print(f"Request failed for draw {n}: {e}")
            break

        if data.get("returnValue") == "fail":
            print(f"No data for draw {n} (stopping).")
            break

        # Normalize fields we care about
        entry = {
            "drwNo": data.get("drwNo"),
            "drwNoDate": data.get("drwNoDate"),
            "nums": [data.get(f"drwtNo{i}") for i in range(1, 7)],
            "bnus": data.get("bnusNo"),
            "totSellamnt": data.get("totSellamnt"),
            "firstWinAmount": data.get("firstWinamnt") or data.get("firstWinamnt"),
        }
        draws.append(entry)
        print(f"Fetched draw {n}")

        n += 1
        if args.end and n > args.end:
            break
        time.sleep(args.delay)

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(draws, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(draws)} draws to {args.out}")


if __name__ == "__main__":
    main()
