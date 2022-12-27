import rucksack


def test_format_input():
    rpcIntance = rucksack.Rucksack('./03/input_mock.txt')
    assert rpcIntance.getRucksacks() == [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]


def test_get_item_importance_number():
    rpcIntance = rucksack.Rucksack('./03/input_mock.txt')
    assert rpcIntance.getItemImportanceNumber('p') == 16
    assert rpcIntance.getItemImportanceNumber('L') == 38
    assert rpcIntance.getItemImportanceNumber('P') == 42
    assert rpcIntance.getItemImportanceNumber('v') == 22
    assert rpcIntance.getItemImportanceNumber('t') == 20
    assert rpcIntance.getItemImportanceNumber('s') == 19


def test_get_total_importance_number():
    rpcIntance = rucksack.Rucksack('./03/input_mock.txt')
    assert rpcIntance.getTotalImportanceNumber() == 157


def test_get_total_importance_number_groupes():
    rpcIntance = rucksack.Rucksack('./03/input_mock.txt')
    assert rpcIntance.getTotalImportanceNumberGroupes() == 70
