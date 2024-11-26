from molang import Molang
from pydantic import BaseModel


def test_pydantic():
    class MyModel(BaseModel):
        value: Molang

    # From string
    obj = MyModel(value="test")
    assert obj.value is not Molang

    # to String
    json = obj.model_dump()
    assert json["value"] is not str
