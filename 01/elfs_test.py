import elfs


def test_format_elfs_input():
    elfsInstance = elfs.Elfs('./01/input_mock')
    assert elfsInstance.getElfs() == [1000, 2000, 3000, 4000]


def test_get_biggest_elf():
    elfsInstance = elfs.Elfs('./01/input_mock')
    assert elfsInstance.getBiggestElf() == 4000


def test_get_top_three_amount():
    elfsInstance = elfs.Elfs('./01/input_mock')
    assert elfsInstance.getTopThreeElfsAmount() == 9000
