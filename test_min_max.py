import min_and_max_from_list
import unittest.mock as mock

def test_output(capsys):
    with mock.patch('builtins.input', side_effect=["1", "2", "3", 'bad data', 'done']):
        min_and_max_from_list.compute_min_and_max()
        captured = capsys.readouterr()
        statements = captured.out.split("\n")

        assert "Maximum: 3.0" in statements
        assert "Minimum: 1.0" in statements

def test_edge_cases(capsys):
    with mock.patch('builtins.input', side_effect=["1", "-20", "300", "300.1", 'done']):
        min_and_max_from_list.compute_min_and_max()
        captured = capsys.readouterr()
        statements = captured.out.split("\n")

        assert "Maximum: 300.1" in statements
        assert "Minimum: -20.0" in statements
