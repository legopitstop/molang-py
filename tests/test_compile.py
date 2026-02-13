from molang import compile


def test_alias():
    a = compile("c.test")
    b = compile("q.test")
    c = compile("t.test")
    d = compile("v.test")

    e = compile("context.test")
    f = compile("query.test")
    g = compile("temp.test")
    h = compile("variable.test")

    assert a == "context.test"
    assert b == "query.test"
    assert c == "temp.test"
    assert d == "variable.test"

    assert e == "context.test"
    assert f == "query.test"
    assert g == "temp.test"
    assert h == "variable.test"
