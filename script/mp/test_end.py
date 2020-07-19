import pytest
from utils import DriverUtils


@pytest.mark.run(order=99)
class TestEnd:

    def test_end(self):
        # 修改关闭浏览器的开关的值未True
        DriverUtils.change_mp_key(True)
        DriverUtils.quit_mp_driver()