from whitercanada.check_commit_message import check


def test_check_merge():
    assert check("Merge <blabla>", {"allow_merge": False}) == 1
    assert check("Merge <blabla>", {"allow_merge": True}) == 0


def test_check_commit_not_formatted():
    assert check("no format") == 1
    assert check("no, format") == 1


def test_check_commit_formatted():
    assert check("prefix: no") == 1
    assert check("prefix: yes", {"prefixes": ["prefix"]}) == 0
    assert check("multiple: prefix", {"prefixes": ["prefix", "multiple"]}) == 0
