import pathlib
import pytest
import morse_encoder

EX_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    morse_test = (EX_DIR / "example1.txt").read_text().splitlines()
    return dict([t.split(' = ') for t in morse_test])

# @pytest.mark.skip(reason="Not implemented")
def test_morse_encode(example1):
    print (example1)
    for test in example1:
        assert morse_encoder.encode(test) == example1[test]
    