#!/usr/bin/env python3
"""Filter a full lotto history JSON to the most recent N months.

Usage:
  python filter_recent.py --months 3 --in history_full.json --out history.json
"""
import argparse
import json
from datetime import datetime, timedelta


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--months', type=int, default=3)
    parser.add_argument('--in', dest='infile', default='history.json')
    parser.add_argument('--out', dest='outfile', default='history.json')
    args = parser.parse_args()

    try:
        with open(args.infile, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print('Failed to read input:', e)
        return

    # approximate months as 30 days
    cutoff = datetime.now().date() - timedelta(days=args.months * 30)
    filtered = []
    for entry in data:
        dstr = entry.get('drwNoDate')
        if not dstr:
            continue
        try:
            d = datetime.fromisoformat(dstr).date()
        except Exception:
            # try YYYY-MM-DD split
            try:
                parts = [int(p) for p in dstr.split('-')]
                d = datetime(parts[0], parts[1], parts[2]).date()
            except Exception:
                continue
        if d >= cutoff:
            filtered.append(entry)

    filtered = sorted(filtered, key=lambda x: x.get('drwNo', 0), reverse=True)

    with open(args.outfile, 'w', encoding='utf-8') as f:
        json.dump(filtered, f, indent=2, ensure_ascii=False)

    print(f'Wrote {len(filtered)} draws to {args.outfile} (cutoff {cutoff})')


if __name__ == '__main__':
    main()
