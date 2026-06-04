
import pytest
class TestB:
    # scope，需要跨模块时，不在当前模块使用
    @pytest.mark.dependency(depends=['t001'],scope="session")
    def test_b01(self):
        print('test_001')

