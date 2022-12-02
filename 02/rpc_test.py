import rpc


def test_format_input():
    rpcIntance = rpc.RockPaperScissors('./02/input_mock')
    assert rpcIntance.getGuide() == [['A', 'X'], ['A', 'Z'], ['A', 'Z']]


def test_play_round():
    rpcIntance = rpc.RockPaperScissors('./01/input_mock')
    rpcIntance.playRound(['A', 'X'])
    assert rpcIntance.getScore() == 7


def test_play_multiple_rounds():
    rpcIntance = rpc.RockPaperScissors('./02/input_mock')
    rpcIntance.playMultipleRounds()
    assert rpcIntance.getScore() == 13
