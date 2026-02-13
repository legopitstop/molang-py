__all__ = ["create_context"]

from typing import Dict, Any
import math
import random as _random


def _ease_in_out_quad(start: float, end: float, value: float) -> float:
    """Ease in-out quadratic interpolation."""
    v = value * 2
    if v < 1:
        return (end - start) * 0.5 * v * v + start
    v -= 1
    return -(end - start) * 0.5 * (v * (v - 2) - 1) + start


def _ease_in_back(start: float, end: float, value: float) -> float:
    """Ease in back (cubic with overshoot)."""
    c1 = 1.70158
    c3 = c1 + 1
    t = value
    return (end - start) * (c3 * t * t * t - c1 * t * t) + start


def _ease_out_back(start: float, end: float, value: float) -> float:
    """Ease out back (cubic with overshoot)."""
    c1 = 1.70158
    c3 = c1 + 1
    t = value - 1
    return (end - start) * (1 + c3 * t * t * t + c1 * t * t) + start


def _ease_in_out_back(start: float, end: float, value: float) -> float:
    """Ease in-out back."""
    c1 = 1.70158
    c2 = c1 * 1.525
    t = value * 2
    if t < 1:
        return (end - start) * 0.5 * (t * t * ((c2 + 1) * t - c2)) + start
    t -= 2
    return (end - start) * 0.5 * (t * t * ((c2 + 1) * t + c2) + 2) + start


def _ease_in_bounce(start: float, end: float, value: float) -> float:
    """Ease in bounce."""
    return (end - start) * (1 - _ease_out_bounce(0, 1, 1 - value)) + start


def _ease_out_bounce(start: float, end: float, value: float) -> float:
    """Ease out bounce."""
    n1 = 7.5625
    d1 = 2.75
    t = value
    if t < 1 / d1:
        res = n1 * t * t
    elif t < 2 / d1:
        t -= 1.5 / d1
        res = n1 * t * t + 0.75
    elif t < 2.5 / d1:
        t -= 2.25 / d1
        res = n1 * t * t + 0.9375
    else:
        t -= 2.625 / d1
        res = n1 * t * t + 0.984375
    return (end - start) * res + start


def _ease_in_out_bounce(start: float, end: float, value: float) -> float:
    """Ease in-out bounce."""
    if value < 0.5:
        return _ease_in_bounce(start, end, value * 2) * 0.5 + start * 0.5
    return (
        _ease_out_bounce(start, end, value * 2 - 1) * 0.5
        + (end - start) * 0.5
        + start * 0.5
    )


def _ease_in_circ(start: float, end: float, value: float) -> float:
    """Ease in circular."""
    return (end - start) * (1 - math.sqrt(1 - value * value)) + start


def _ease_out_circ(start: float, end: float, value: float) -> float:
    """Ease out circular."""
    t = value - 1
    return (end - start) * math.sqrt(1 - t * t) + start


def _ease_in_out_circ(start: float, end: float, value: float) -> float:
    """Ease in-out circular."""
    t = value * 2
    if t < 1:
        return (end - start) * 0.5 * (1 - math.sqrt(1 - t * t)) + start
    t -= 2
    return (end - start) * 0.5 * (math.sqrt(1 - t * t) + 1) + start


def _ease_in_cubic(start: float, end: float, value: float) -> float:
    """Ease in cubic."""
    return (end - start) * value * value * value + start


def _ease_out_cubic(start: float, end: float, value: float) -> float:
    """Ease out cubic."""
    t = value - 1
    return (end - start) * (t * t * t + 1) + start


def _ease_in_out_cubic(start: float, end: float, value: float) -> float:
    """Ease in-out cubic."""
    t = value * 2
    if t < 1:
        return (end - start) * 0.5 * t * t * t + start
    t -= 2
    return (end - start) * 0.5 * (t * t * t + 2) + start


def _ease_in_elastic(start: float, end: float, value: float) -> float:
    """Ease in elastic."""
    if value == 0:
        return start
    if value == 1:
        return end
    c4 = (2 * math.pi) / 3
    t = value
    return (
        -(end - start) * (2 ** (10 * t - 10)) * math.sin((t * 10 - 10.75) * c4) + start
    )


def _ease_out_elastic(start: float, end: float, value: float) -> float:
    """Ease out elastic."""
    if value == 0:
        return start
    if value == 1:
        return end
    c4 = (2 * math.pi) / 3
    t = value
    return (
        (end - start) * (2 ** (-10 * t)) * math.sin((t * 10 - 0.75) * c4)
        + (end - start)
        + start
    )


def _ease_in_out_elastic(start: float, end: float, value: float) -> float:
    """Ease in-out elastic."""
    if value == 0:
        return start
    if value == 1:
        return end
    c5 = (2 * math.pi) / 4.5
    t = value * 2
    if t < 1:
        return (
            -(end - start)
            * 0.5
            * (2 ** (10 * t - 10))
            * math.sin((t * 10 - 11.125) * c5)
            + start
        )
    t -= 1
    return (
        (end - start) * 0.5 * (2 ** (-10 * t)) * math.sin((t * 10 - 0.125) * c5)
        + (end - start) * 0.5
        + start
    )


def _ease_in_expo(start: float, end: float, value: float) -> float:
    """Ease in exponential."""
    if value == 0:
        return start
    return (end - start) * (2 ** (10 * value - 10)) + start


def _ease_out_expo(start: float, end: float, value: float) -> float:
    """Ease out exponential."""
    if value == 1:
        return end
    return (end - start) * (1 - 2 ** (-10 * value)) + start


def _ease_in_out_expo(start: float, end: float, value: float) -> float:
    """Ease in-out exponential."""
    if value == 0:
        return start
    if value == 1:
        return end
    t = value * 2
    if t < 1:
        return (end - start) * 0.5 * (2 ** (10 * t - 10)) + start
    t -= 1
    return (end - start) * 0.5 * (1 - 2 ** (-10 * t)) + start


def _ease_in_quart(start: float, end: float, value: float) -> float:
    """Ease in quartic."""
    return (end - start) * value * value * value * value + start


def _ease_out_quart(start: float, end: float, value: float) -> float:
    """Ease out quartic."""
    t = value - 1
    return -(end - start) * (t * t * t * t - 1) + start


def _ease_in_out_quart(start: float, end: float, value: float) -> float:
    """Ease in-out quartic."""
    t = value * 2
    if t < 1:
        return (end - start) * 0.5 * t * t * t * t + start
    t -= 2
    return -(end - start) * 0.5 * (t * t * t * t - 2) + start


def _ease_in_quint(start: float, end: float, value: float) -> float:
    """Ease in quintic."""
    return (end - start) * value * value * value * value * value + start


def _ease_out_quint(start: float, end: float, value: float) -> float:
    """Ease out quintic."""
    t = value - 1
    return (end - start) * (t * t * t * t * t + 1) + start


def _ease_in_out_quint(start: float, end: float, value: float) -> float:
    """Ease in-out quintic."""
    t = value * 2
    if t < 1:
        return (end - start) * 0.5 * t * t * t * t * t + start
    t -= 2
    return (end - start) * 0.5 * (t * t * t * t * t + 2) + start


def _ease_in_sine(start: float, end: float, value: float) -> float:
    """Ease in sine."""
    return -(end - start) * math.cos(value * math.pi / 2) + (end - start) + start


def _ease_out_sine(start: float, end: float, value: float) -> float:
    """Ease out sine."""
    return (end - start) * math.sin(value * math.pi / 2) + start


def _ease_in_out_sine(start: float, end: float, value: float) -> float:
    """Ease in-out sine."""
    return -(end - start) * 0.5 * (math.cos(math.pi * value) - 1) + start


def _hermite_blend(value: float) -> float:
    """Hermite blend (smoothstep)."""
    return value * value * (3 - 2 * value)


def _die_roll(num: int, low: float, high: float) -> float:
    """Roll dice num times and sum, each in [low, high]. Returns average."""
    num = max(1, int(num))
    return sum(_random.uniform(low, high) for _ in range(num)) / num


def _die_roll_integer(num: int, low: int, high: int) -> float:
    """Roll dice num times and sum, each in [low, high] inclusive. Returns average."""
    num = max(1, int(num))
    low = int(low)
    high = int(high)
    return sum(_random.randint(low, high) for _ in range(num)) / num


def create_context() -> Dict[str, Any]:
    return {
        "context": {},
        "query": {},
        "temp": {},
        "variable": {},
        "geometry": {},
        "texture": {},
        "material": {},
        "math": {
            "pi": math.pi,
            "abs": abs,
            "acos": math.acos,
            "asin": math.asin,
            "atan": math.atan,
            "atan2": math.atan2,
            "ceil": math.ceil,
            "clamp": lambda value, min_val, max_val: max(min_val, min(max_val, value)),
            "copy_sign": math.copysign,
            "cos": math.cos,
            "die_roll": _die_roll,
            "die_roll_integer": _die_roll_integer,
            "ease_in_back": _ease_in_back,
            "ease_in_bounce": _ease_in_bounce,
            "ease_in_circ": _ease_in_circ,
            "ease_in_cubic": _ease_in_cubic,
            "ease_in_elastic": _ease_in_elastic,
            "ease_in_expo": _ease_in_expo,
            "ease_in_out_back": _ease_in_out_back,
            "ease_in_out_bounce": _ease_in_out_bounce,
            "ease_in_out_circ": _ease_in_out_circ,
            "ease_in_out_cubic": _ease_in_out_cubic,
            "ease_in_out_elastic": _ease_in_out_elastic,
            "ease_in_out_expo": _ease_in_out_expo,
            "ease_in_out_quad": _ease_in_out_quad,
            "ease_in_out_quart": _ease_in_out_quart,
            "ease_in_out_quint": _ease_in_out_quint,
            "ease_in_out_sine": _ease_in_out_sine,
            "ease_in_quad": lambda start, end, value: (end - start) * value * value
            + start,
            "ease_in_quart": _ease_in_quart,
            "ease_in_quint": _ease_in_quint,
            "ease_in_sine": _ease_in_sine,
            "ease_out_back": _ease_out_back,
            "ease_out_bounce": _ease_out_bounce,
            "ease_out_circ": _ease_out_circ,
            "ease_out_cubic": _ease_out_cubic,
            "ease_out_elastic": _ease_out_elastic,
            "ease_out_expo": _ease_out_expo,
            "ease_out_quad": lambda start, end, value: -(end - start)
            * value
            * (value - 2)
            + start,
            "ease_out_quart": _ease_out_quart,
            "ease_out_quint": _ease_out_quint,
            "ease_out_sine": _ease_out_sine,
            "exp": math.exp,
            "floor": math.floor,
            "hermite_blend": _hermite_blend,
            "inverse_lerp": lambda start, end, value: (
                (value - start) / (end - start) if end != start else 0
            ),
            "lerp": lambda start, end, value: start + (end - start) * value,
            "lerprotate": lambda start, end, value: start + (end - start) * value,
            "ln": math.log,
            "max": max,
            "min": min,
            "min_angle": lambda value: (value + math.pi) % (2 * math.pi) - math.pi,
            "mod": lambda value, denominator: (
                value % denominator if denominator != 0 else 0
            ),
            "pow": pow,
            "random": lambda low, high: _random.uniform(low, high),
            "random_integer": lambda low, high: _random.randint(int(low), int(high)),
            "round": round,
            "sign": lambda value: 1 if value > 0 else (-1 if value < 0 else 0),
            "sin": math.sin,
            "sqrt": math.sqrt,
            "trunc": math.trunc,
        },
    }
