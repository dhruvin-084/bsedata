import pytest
from bsedata.bse import BSE

b = BSE()

@pytest.mark.parametrize("scripCode",['534976','500116','512573'])
def test_getQuote_valid(scripCode):
    assert len(b.getQuote(scripCode)) == 27

def test_getQuote_invalid():
    assert len(b.getQuote('513715')) == 27

def test_verifyCode_valid():
    assert b.verifyScripCode('534976') == 'V-mart Retail Ltd.'

def test_verifyCode_invalid():
    assert b.verifyScripCode('534980') == None