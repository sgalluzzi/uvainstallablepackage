import sys
sys.path.append('.')
import shared as sh

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)

 
#B
def test_addition():
    result = 5 + 4
    assert result == 9

@pytest.mark.xfail    
def test_subtraction():
    result = 5 - 2
    assert result == 3
    
#C    
@pytest.mark.skip(reason="Skip the bad math!")    
def test_multiplication():
    result = 5 * 2
    assert result == 10

#D
@pytest.mark.skipif(sys.platform == "darwin",reason="He has evolved past division.")
def test_division():
    print(sys.platform)
    result = 20 / 4
    assert result == 5
