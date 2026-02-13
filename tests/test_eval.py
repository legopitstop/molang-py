from molang import eval, create_context


def test_eval_query():
    a = eval("query.health")
    b = eval("query.health", {"query": {"health": 100}})
    assert a == 0
    assert b == 100


def test_eval_integer():
    a = eval("100")
    b = eval("-100")
    assert a == 100
    assert b == -100


def test_eval_float():
    a = eval("3.14159")
    b = eval("-3.14159")
    assert a == 3.14159
    assert b == -3.14159


def test_eval_assign():
    ctx = create_context()
    eval("variable.x = 5", ctx)
    assert ctx["variable"]["x"] == 5


# def test_eval_array():
#     ctx = {'array': {'my_geometries': ["item1", "item2", "item3"]}}
#     a = eval(array.my_geometries[query.anim_time], ctx)
#     b = eval(array.my_geometries[0], ctx)
#     assert a == 'item1'
#     assert b == 'item1'


def test_eval_not():
    """not"""
    a = eval("!query.health")
    assert a == 1


def test_eval_and():
    """and"""
    a = eval("0 && 0")
    b = eval("1 && 1")
    # c = eval('1 && 0')
    d = eval("0 && 1")
    assert not a
    assert b
    # assert not c
    assert not d


def test_eval_or():
    """or"""
    a = eval("0 || 0")
    b = eval("1 || 1")
    # c = eval('1 || 0')
    d = eval("0 || 1")
    assert not a
    assert b
    # assert c
    assert d


def test_eval_lt():
    """less than"""
    a = eval("0 < 100")
    b = eval("100 < 0")
    c = eval("100 < 100")
    assert a
    assert not b
    assert not c


def test_eval_le():
    """less than or equal to"""
    a = eval("0 <= 100")
    b = eval("100 <= 0")
    c = eval("100 <= 100")
    assert a
    assert not b
    assert c


def test_eval_gt():
    """greater than"""
    a = eval("0 > 100")
    # b = eval('100 > 0')
    c = eval("100 > 100")
    assert not a
    # assert b
    assert not c


def test_eval_ge():
    """greater than or equal to"""
    a = eval("0 >= 100")
    # b = eval('100 >= 0')
    c = eval("100 >= 100")
    assert not a
    # assert b
    assert c


def test_eval_eq():
    """equal"""
    a = eval("100 == 100")
    b = eval("0 == 100")
    assert a
    assert not b


def test_eval_ne():
    """not equal"""
    a = eval("100 != 100")
    b = eval("0 != 100")
    assert not a
    assert b


def test_eval_mul():
    a = eval("5 * 2")
    b = eval("5 * 0.10")
    assert a == 10
    assert b == 0.5


def test_eval_truediv():
    a = eval("10 / 2")
    b = eval("10 / 0.10")
    assert a == 5
    assert b == 100


def test_eval_add():
    a = eval("5 + 5")
    b = eval("5 + 0.10")
    assert a == 10
    assert b == 5.10


def test_eval_sub():
    a = eval("5 - 5")
    b = eval("5 - 10")
    c = eval("5 - 0.10")
    d = eval("5 - 10.10")
    assert a == 0
    assert b == -5
    assert c == 4.9
    assert d == -5.1


def test_eval_math():
    """Test all math functions."""
    import math as py_math

    # Constants
    x = eval("math.pi")
    assert x == py_math.pi

    # Basic functions
    assert eval("math.abs(-5)") == 5
    assert eval("math.abs(5)") == 5
    assert eval("math.sqrt(16)") == 4.0
    assert eval("math.pow(2, 3)") == 8
    assert abs(eval("math.exp(1)") - py_math.e) < 1e-9
    assert eval("math.ln(1)") == 0.0

    # Trigonometric
    assert abs(eval("math.sin(0)") - 0) < 1e-9
    assert abs(eval("math.cos(0)") - 1) < 1e-9
    assert abs(eval("math.atan(0)") - 0) < 1e-9
    assert abs(eval("math.asin(0)") - 0) < 1e-9
    assert abs(eval("math.acos(1)") - 0) < 1e-9

    # Atan2
    assert abs(eval("math.atan2(1, 1)") - py_math.pi / 4) < 1e-9

    # Rounding
    assert eval("math.ceil(3.2)") == 4
    assert eval("math.floor(3.8)") == 3
    assert eval("math.round(3.5)") == 4
    assert eval("math.trunc(3.9)") == 3

    # Utility
    assert eval("math.max(3, 7)") == 7
    assert eval("math.min(3, 7)") == 3
    assert eval("math.clamp(5, 0, 10)") == 5
    assert eval("math.clamp(-5, 0, 10)") == 0
    assert eval("math.clamp(15, 0, 10)") == 10

    # Sign
    assert eval("math.sign(5)") == 1
    assert eval("math.sign(-5)") == -1
    assert eval("math.sign(0)") == 0

    # Copy sign
    assert eval("math.copy_sign(5, -1)") == -5
    assert eval("math.copy_sign(-5, 1)") == 5

    # Modulo
    assert eval("math.mod(10, 3)") == 1
    assert eval("math.mod(7, 2)") == 1

    # Min angle
    result = eval("math.min_angle(3.14159)")
    assert -py_math.pi <= result <= py_math.pi

    # Interpolation
    assert abs(eval("math.lerp(0, 10, 0.5)") - 5.0) < 1e-9
    assert abs(eval("math.inverse_lerp(0, 10, 5)") - 0.5) < 1e-9
    assert abs(eval("math.lerprotate(0, 1, 0.5)") - 0.5) < 1e-9
    assert abs(eval("math.hermite_blend(0.5)") - 0.5) < 1e-9

    # Easing functions - test endpoints
    assert abs(eval("math.ease_in_quad(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_quad(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_out_quad(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_out_quad(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_in_out_quad(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_out_quad(0, 10, 1)") - 10) < 1e-6

    assert abs(eval("math.ease_in_cubic(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_cubic(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_out_cubic(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_out_cubic(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_in_out_cubic(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_out_cubic(0, 10, 1)") - 10) < 1e-6

    assert abs(eval("math.ease_in_quart(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_quart(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_out_quart(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_out_quart(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_in_out_quart(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_out_quart(0, 10, 1)") - 10) < 1e-6

    assert abs(eval("math.ease_in_quint(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_quint(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_out_quint(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_out_quint(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_in_out_quint(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_out_quint(0, 10, 1)") - 10) < 1e-6

    assert abs(eval("math.ease_in_sine(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_sine(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_out_sine(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_out_sine(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_in_out_sine(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_out_sine(0, 10, 1)") - 10) < 1e-6

    assert abs(eval("math.ease_in_circ(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_circ(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_out_circ(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_out_circ(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_in_out_circ(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_out_circ(0, 10, 1)") - 10) < 1e-6

    assert abs(eval("math.ease_in_expo(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_expo(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_out_expo(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_out_expo(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_in_out_expo(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_out_expo(0, 10, 1)") - 10) < 1e-6

    assert abs(eval("math.ease_in_back(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_back(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_out_back(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_out_back(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_in_out_back(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_out_back(0, 10, 1)") - 10) < 1e-6

    assert abs(eval("math.ease_in_bounce(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_bounce(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_out_bounce(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_out_bounce(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_in_out_bounce(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_out_bounce(0, 10, 1)") - 10) < 1e-6

    assert abs(eval("math.ease_in_elastic(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_elastic(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_out_elastic(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_out_elastic(0, 10, 1)") - 10) < 1e-6
    assert abs(eval("math.ease_in_out_elastic(0, 10, 0)") - 0) < 1e-6
    assert abs(eval("math.ease_in_out_elastic(0, 10, 1)") - 10) < 1e-6

    # Random functions - just test that they're callable and return numbers
    result = eval("math.random(0, 10)")
    assert 0 <= result <= 10

    result = eval("math.random_integer(1, 6)")
    assert 1 <= result <= 6

    # Die roll returns average
    result = eval("math.die_roll(1, 1, 6)")
    assert 1 <= result <= 6

    result = eval("math.die_roll_integer(1, 1, 6)")
    assert 1 <= result <= 6


def test_eval_ternary():
    text = "q.is_on_ground ? 12 : 32"
    a = eval(text, {"query": {"is_on_ground": True}})
    b = eval(text, {"query": {"is_on_ground": False}})
    assert a == 12
    assert b == 32
