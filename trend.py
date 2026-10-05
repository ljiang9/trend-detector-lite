"""trend-detector-lite — 趋势 / 突变检测。

移动平均、方向判断、简单变点与突增突降检测。零第三方依赖。
"""
from __future__ import annotations


def moving_average(series: list[float], window: int = 3) -> list[float]:
    """滑窗移动平均，窗口不足时取已有均值。"""
    out = []
    for i in range(len(series)):
        lo = max(0, i - window + 1)
        seg = series[lo:i + 1]
        out.append(round(sum(seg) / len(seg), 3))
    return out


def direction(series: list[float]) -> str:
    """比较首尾判断整体方向。"""
    if len(series) < 2:
        return "flat"
    diff = series[-1] - series[0]
    if abs(diff) < 1e-9:
        return "flat"
    return "up" if diff > 0 else "down"


def detect_spikes(series: list[float], threshold: float = 2.0) -> list[int]:
    """突增突降：相邻差分超过相邻差分绝对值中位数*threshold 视为突变点索引。"""
    if len(series) < 3:
        return []
    diffs = [series[i] - series[i - 1] for i in range(1, len(series))]
    abs_diffs = sorted(abs(d) for d in diffs)
    med = abs_diffs[len(abs_diffs) // 2] or 1e-9
    spikes = []
    for i, d in enumerate(diffs, start=1):
        if abs(d) > med * threshold:
            spikes.append(i)
    return spikes


def analyze(series: list[float], window: int = 3) -> dict:
    return {
        "series": series,
        "moving_average": moving_average(series, window),
        "direction": direction(series),
        "spikes": detect_spikes(series),
    }
