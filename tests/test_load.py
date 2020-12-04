"""Test."""
from small_kg import hetio


def test_load():
    """Test data loading."""
    with open(hetio.nodes_file, "r") as stream:
        data = stream.read()
    assert data
