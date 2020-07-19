import pytest
from utils import DriverUtils


@pytest.mark.run(order=100)
class TestBegin:

    def test_begin(self):
        # 修改关闭浏览器的开关的值未False
        DriverUtils.change_mis_key(False)