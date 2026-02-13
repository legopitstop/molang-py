from molang.dsl import (
    MolangExpr,
    array,
    math,
    query,
    variable,
    geometry,
    temp,
    context,
    texture,
    material,
)
from pydantic import BaseModel


def test_query():
    a = query.health
    b = query.HEALTH
    c = query.block_state("facing")
    assert a.expr == "query.health"
    assert b.expr == "query.health"
    assert c.expr == "query.block_state('facing')"

    # Custom

    d = query.custom
    e = query.custom_call("arg1")
    assert d.expr == "query.custom"
    assert e.expr == "query.custom_call('arg1')"


def test_variable():
    a = variable.test
    b = temp.test
    c = context.test
    d = geometry.test
    e = texture.test
    f = material.test
    assert a.expr == "variable.test"
    assert b.expr == "temp.test"
    assert c.expr == "context.test"
    assert d.expr == "geometry.test"
    assert e.expr == "texture.test"
    assert f.expr == "material.test"


def test_variable_call():
    a = variable.test("arg1", 1, 0.5, True)
    b = temp.test("arg1", 1, 0.5, True)
    c = context.test("arg1", 1, 0.5, True)
    d = geometry.test("arg1", 1, 0.5, True)
    e = texture.test("arg1", 1, 0.5, True)
    f = material.test("arg1", 1, 0.5, True)
    assert a.expr == "variable.test('arg1', 1, 0.5, 1)"
    assert b.expr == "temp.test('arg1', 1, 0.5, 1)"
    assert c.expr == "context.test('arg1', 1, 0.5, 1)"
    assert d.expr == "geometry.test('arg1', 1, 0.5, 1)"
    assert e.expr == "texture.test('arg1', 1, 0.5, 1)"
    assert f.expr == "material.test('arg1', 1, 0.5, 1)"


def test_type_integer():
    a = MolangExpr(100)
    b = MolangExpr(-100)
    assert a.expr == "100"
    assert b.expr == "-100"


def test_type_float():
    a = MolangExpr(3.14159)
    b = MolangExpr(-3.14159)
    assert a.expr == "3.14159"
    assert b.expr == "-3.14159"


def test_type_string():
    a = MolangExpr("'hello'")
    b = MolangExpr("'HELLO'")
    assert a.expr == "'hello'"
    assert b.expr == "'HELLO'"


def test_type_boolean():
    a = MolangExpr("true")
    b = MolangExpr("false")
    c = MolangExpr(True)
    d = MolangExpr(False)
    assert a.expr == "1"
    assert b.expr == "0"
    assert c.expr == "1"
    assert d.expr == "0"


def test_type_array():
    a = array.my_geometries[query.anim_time]
    b = array.my_geometries[0]
    c = array.my_geometries[0.0]
    assert a.expr == "array.my_geometries[query.anim_time]"
    assert b.expr == "array.my_geometries[0]"
    assert c.expr == "array.my_geometries[0.0]"


def test_logical_not():
    """not"""
    a = ~query.health
    assert a.expr == "!query.health"


def test_logical_and():
    """and"""
    a = query.health & 100
    b = query.health & query.is_on_ground
    assert a.expr == "query.health && 100"
    assert b.expr == "query.health && query.is_on_ground"


def test_logical_or():
    """or"""
    a = query.health | 100
    b = query.health | query.is_on_ground
    assert a.expr == "query.health || 100"
    assert b.expr == "query.health || query.is_on_ground"


def test_logical_lt():
    """less than"""
    a = query.health < 100
    b = query.health < query.is_on_ground
    assert a.expr == "query.health < 100"
    assert b.expr == "query.health < query.is_on_ground"


def test_logical_le():
    """less than or equal to"""
    a = query.health <= 100
    b = query.health <= query.is_on_ground
    assert a.expr == "query.health <= 100"
    assert b.expr == "query.health <= query.is_on_ground"


def test_logical_gt():
    """greater than"""
    a = query.health > 100
    b = query.health > query.is_on_ground
    assert a.expr == "query.health > 100"
    assert b.expr == "query.health > query.is_on_ground"


def test_logical_ge():
    """greater than or equal to"""
    a = query.health >= 100
    b = query.health >= query.is_on_ground
    assert a.expr == "query.health >= 100"
    assert b.expr == "query.health >= query.is_on_ground"


def test_logical_eq():
    """equal"""
    a = query.health == 100
    b = query.health == query.is_on_ground
    assert a.expr == "query.health == 100"
    assert b.expr == "query.health == query.is_on_ground"


def test_logical_ne():
    """not equal"""
    a = query.health != 100
    b = query.health != query.is_on_ground
    assert a.expr == "query.health != 100"
    assert b.expr == "query.health != query.is_on_ground"


def test_bin_mul():
    a = query.health * 100
    b = query.health * query.is_on_ground
    assert a.expr == "(query.health * 100)"
    assert b.expr == "(query.health * query.is_on_ground)"


def test_bin_truediv():
    a = query.health / 100
    b = query.health / query.is_on_ground
    assert a.expr == "(query.health / 100)"
    assert b.expr == "(query.health / query.is_on_ground)"


def test_bin_floordiv():
    a = query.health // 100
    b = query.health // query.is_on_ground
    assert a.expr == "(query.health / 100)"
    assert b.expr == "(query.health / query.is_on_ground)"


def test_bin_add():
    a = query.health + 100
    b = query.health + query.is_on_ground
    assert a.expr == "(query.health + 100)"
    assert b.expr == "(query.health + query.is_on_ground)"


def test_bin_sub():
    a = query.health - 100
    b = query.health - query.is_on_ground
    assert a.expr == "(query.health - 100)"
    assert b.expr == "(query.health - query.is_on_ground)"


def test_math():
    x = math.pi
    assert x.expr == "math.pi"

    x = math.abs(1)
    assert x.expr == "math.abs(1)"

    x = math.acos(1)
    assert x.expr == "math.acos(1)"

    x = math.asin(1)
    assert x.expr == "math.asin(1)"

    x = math.atan(1)
    assert x.expr == "math.atan(1)"

    x = math.atan2(1, 2)
    assert x.expr == "math.atan2(1, 2)"

    x = math.ceil(1)
    assert x.expr == "math.ceil(1)"

    x = math.clamp(1, 2, 3)
    assert x.expr == "math.clamp(1, 2, 3)"

    x = math.copy_sign(1, 2)
    assert x.expr == "math.copy_sign(1, 2)"

    x = math.cos(1)
    assert x.expr == "math.cos(1)"

    x = math.die_roll(1, 2, 3)
    assert x.expr == "math.die_roll(1, 2, 3)"

    x = math.die_roll_integer(1, 2, 3)
    assert x.expr == "math.die_roll_integer(1, 2, 3)"

    x = math.ease_in_back(1, 2, 3)
    assert x.expr == "math.ease_in_back(1, 2, 3)"

    x = math.ease_in_bounce(1, 2, 3)
    assert x.expr == "math.ease_in_bounce(1, 2, 3)"

    x = math.ease_in_circ(1, 2, 3)
    assert x.expr == "math.ease_in_circ(1, 2, 3)"

    x = math.ease_in_cubic(1, 2, 3)
    assert x.expr == "math.ease_in_cubic(1, 2, 3)"

    x = math.ease_in_elastic(1, 2, 3)
    assert x.expr == "math.ease_in_elastic(1, 2, 3)"

    x = math.ease_in_expo(1, 2, 3)
    assert x.expr == "math.ease_in_expo(1, 2, 3)"

    x = math.ease_in_out_back(1, 2, 3)
    assert x.expr == "math.ease_in_out_back(1, 2, 3)"

    x = math.ease_in_out_bounce(1, 2, 3)
    assert x.expr == "math.ease_in_out_bounce(1, 2, 3)"

    x = math.ease_in_out_circ(1, 2, 3)
    assert x.expr == "math.ease_in_out_circ(1, 2, 3)"

    x = math.ease_in_out_cubic(1, 2, 3)
    assert x.expr == "math.ease_in_out_cubic(1, 2, 3)"

    x = math.ease_in_out_elastic(1, 2, 3)
    assert x.expr == "math.ease_in_out_elastic(1, 2, 3)"

    x = math.ease_in_out_expo(1, 2, 3)
    assert x.expr == "math.ease_in_out_expo(1, 2, 3)"

    x = math.ease_in_out_quad(1, 2, 3)
    assert x.expr == "math.ease_in_out_quad(1, 2, 3)"

    x = math.ease_in_out_quart(1, 2, 3)
    assert x.expr == "math.ease_in_out_quart(1, 2, 3)"

    x = math.ease_in_out_quint(1, 2, 3)
    assert x.expr == "math.ease_in_out_quint(1, 2, 3)"

    x = math.ease_in_out_sine(1, 2, 3)
    assert x.expr == "math.ease_in_out_sine(1, 2, 3)"

    x = math.ease_in_quad(1, 2, 3)
    assert x.expr == "math.ease_in_quad(1, 2, 3)"

    x = math.ease_in_quart(1, 2, 3)
    assert x.expr == "math.ease_in_quart(1, 2, 3)"

    x = math.ease_in_quint(1, 2, 3)
    assert x.expr == "math.ease_in_quint(1, 2, 3)"

    x = math.ease_in_sine(1, 2, 3)
    assert x.expr == "math.ease_in_sine(1, 2, 3)"

    x = math.ease_out_back(1, 2, 3)
    assert x.expr == "math.ease_out_back(1, 2, 3)"

    x = math.ease_out_bounce(1, 2, 3)
    assert x.expr == "math.ease_out_bounce(1, 2, 3)"

    x = math.ease_out_circ(1, 2, 3)
    assert x.expr == "math.ease_out_circ(1, 2, 3)"

    x = math.ease_out_cubic(1, 2, 3)
    assert x.expr == "math.ease_out_cubic(1, 2, 3)"

    x = math.ease_out_elastic(1, 2, 3)
    assert x.expr == "math.ease_out_elastic(1, 2, 3)"

    x = math.ease_out_expo(1, 2, 3)
    assert x.expr == "math.ease_out_expo(1, 2, 3)"

    x = math.ease_out_quad(1, 2, 3)
    assert x.expr == "math.ease_out_quad(1, 2, 3)"

    x = math.ease_out_quart(1, 2, 3)
    assert x.expr == "math.ease_out_quart(1, 2, 3)"

    x = math.ease_out_quint(1, 2, 3)
    assert x.expr == "math.ease_out_quint(1, 2, 3)"

    x = math.ease_out_sine(1, 2, 3)
    assert x.expr == "math.ease_out_sine(1, 2, 3)"

    x = math.exp(1)
    assert x.expr == "math.exp(1)"

    x = math.floor(1)
    assert x.expr == "math.floor(1)"

    x = math.hermite_blend(1)
    assert x.expr == "math.hermite_blend(1)"

    x = math.inverse_lerp(1, 2, 3)
    assert x.expr == "math.inverse_lerp(1, 2, 3)"

    x = math.lerp(1, 2, 3)
    assert x.expr == "math.lerp(1, 2, 3)"

    x = math.lerprotate(1, 2, 3)
    assert x.expr == "math.lerprotate(1, 2, 3)"

    x = math.ln(1)
    assert x.expr == "math.ln(1)"

    x = math.max(1, 2)
    assert x.expr == "math.max(1, 2)"

    x = math.min(1, 2)
    assert x.expr == "math.min(1, 2)"

    x = math.min_angle(1)
    assert x.expr == "math.min_angle(1)"

    x = math.mod(1, 2)
    assert x.expr == "math.mod(1, 2)"

    x = math.pow(1, 2)
    assert x.expr == "math.pow(1, 2)"

    x = math.random(1, 2)
    assert x.expr == "math.random(1, 2)"

    x = math.random_integer(1, 2)
    assert x.expr == "math.random_integer(1, 2)"

    x = math.round(1)
    assert x.expr == "math.round(1)"

    x = math.sign(1)
    assert x.expr == "math.sign(1)"

    x = math.sin(1)
    assert x.expr == "math.sin(1)"

    x = math.sqrt(1)
    assert x.expr == "math.sqrt(1)"

    x = math.trunc(1)
    assert x.expr == "math.trunc(1)"

    # Custom

    x = math.custom(1)
    assert x.expr == "math.custom(1)"


def test_ternary():
    x = query.is_on_ground.if_(12, 32)
    assert x.expr == "(query.is_on_ground ? 12 : 32)"


def test_assign():
    variable.test = 4
    assert variable.test.expr == "variable.test = 4;"

    variable.test = "Hello, World!"
    assert variable.test.expr == "variable.test = 'Hello, World!';"


def test_itr():
    x = MolangExpr.loop(10, MolangExpr("t.x = v.x + v.y;v.x = v.y; v.y = t.x;"))
    assert x.expr == "loop(10, {t.x = v.x + v.y;v.x = v.y; v.y = t.x;});"

    x = MolangExpr.for_each(
        temp.pig,
        query.get_nearby_entities(4, "minecraft:pig"),
        MolangExpr("variable.x = variable.x + 1;"),
    )
    assert (
        x.expr
        == "for_each(temp.pig, query.get_nearby_entities(4, 'minecraft:pig'), {variable.x = variable.x + 1;});"
    )


def test_expr():
    x = ~query.equipped_item_all_tags("slot.armor.chest", "paper") | query.is_on_ground
    assert (
        x.expr
        == "!query.equipped_item_all_tags('slot.armor.chest', 'paper') || query.is_on_ground"
    )

    x = query.block_state("minecraft:cardinal_direction") == "north"
    assert x.expr == "query.block_state('minecraft:cardinal_direction') == 'north'"

    x = (
        math.cos(query.anim_time * 38) * variable.rotation_scale
        + variable.x * variable.x * query.life_time
    )
    assert (
        x.expr
        == "((math.cos((query.anim_time * 38)) * variable.rotation_scale) + ((variable.x * variable.x) * query.life_time))"
    )

    x = query.is_sleeping.if_(
        geometry.my_sleeping_geo,
        array.my_geos[math.cos(query.anim_time * 12.3 + 41.9) * 10 + 0.6],
    )
    assert (
        x.expr
        == "(query.is_sleeping ? geometry.my_sleeping_geo : array.my_geos[((math.cos(((query.anim_time * 12.3) + 41.9)) * 10) + 0.6)])"
    )

    # v.x = 0;
    # for_each(v.pig, query.get_nearby_entities(4, 'minecraft:pig'), {
    #     v.x = v.x + v.pig->query.get_relative_block_state(0, 1, 0, 'flammable');
    # });
    #
    # (v.moo > 0) ? {
    #   v.x = math.sin(q.life_time * 45);
    #   v.x = v.x * v.x + 17.3;
    #   t.sin_x = math.sin(v.x);
    #   v.x = t.sin_x * t.sin_x + v.x * v.x;
    #   v.x = math.sqrt(v.x) * v.x * math.pi;
    # }
    #
    # v.x = 1;
    # v.y = 1;
    # loop(10, {
    #   t.x = v.x + v.y;
    #   v.x = v.y;
    #   v.y = t.x;
    # });
    #
    # v.x = 0;
    # for_each(t.pig, query.get_nearby_entities(4, 'minecraft:pig'), {
    #     v.x = v.x + 1;
    # });
    #
    # v.x = 1;
    # v.y = 1;
    # loop(10, {t.x = v.x + v.y; v.x = v.y; v.y = t.x; (v.y > 20) ? break;});
    #
    # v.x = 0;
    # loop(10, {
    #   (v.x > 5) ? continue;
    #   v.x = v.x + 1;
    # });
    #
    # x = variable.x = (variable.x or 1.2) + 0.3
    #
    # index = max(0, expression_result) % array_size

    x = array.hair_colors[variable.hair_color]
    assert x.expr == "array.hair_colors[variable.hair_color]"

    x = query.is_baby.if_(-8.0, 0.0)
    assert x.expr == "(query.is_baby ? -8.0 : 0.0)"

    x = math.sin(query.anim_time * 1.23)
    print(x)
    assert x.expr == "math.sin((query.anim_time * 1.23))"


def test_pydantic():
    class Test(BaseModel):
        condition: MolangExpr

    x = Test(condition=query.block_state("facing") == "north")
    assert x.model_dump() == {"condition": "query.block_state('facing') == 'north'"}
