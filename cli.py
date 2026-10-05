"""命令行：python3 cli.py 1,2,3,4,5,20,6"""
import argparse
import json
import sys

from trend import analyze


def main(argv=None):
    p = argparse.ArgumentParser(description="trend-detector-lite 趋势/突变检测")
    p.add_argument("series", help="逗号分隔数值，如 1,2,3,4,20")
    p.add_argument("-w", "--window", type=int, default=3)
    args = p.parse_args(argv)
    raw = args.series
    series = [float(x) for x in raw.split(",") if x.strip()]
    print(json.dumps(analyze(series, args.window), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
