import json

import pytest

import whitercanada


def test_config(mocker, tmp_path):
    config_path = tmp_path / "config"
    mocker.patch("whitercanada.CONFIG_PATH", config_path)

    with pytest.raises(SystemExit) as exc:
        whitercanada.get_config("b")
    assert exc.type is SystemExit
    assert exc.value.code == 1

    with open(config_path, "w") as config:
        json.dump({"a": "b"}, config)

    assert whitercanada.get_config("a") == "b"

    with pytest.raises(SystemExit) as exc:
        whitercanada.get_config("b")
    assert exc.type is SystemExit
    assert exc.value.code == 2
