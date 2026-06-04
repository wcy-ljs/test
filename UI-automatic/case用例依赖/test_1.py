import pytest
# @pytest.mark.dependency()

# def test_001():
#     print('test_001')
#     assert 1==2
#
# @pytest.mark.dependency(depends=['test_001'])
# def test_002():
#     print('test_002')

class TestA:
    @pytest.mark.dependency(name='t001')
    def test_001(self):
        print('test_001')
        assert 1==2
    @pytest.mark.dependency(depends=['t001'])
    def test_002(self):
        print('test_002')

