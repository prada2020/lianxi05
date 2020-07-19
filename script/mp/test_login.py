import time
import pytest
from page.mp.login_page import LoginProxy
from utils import DriverUtils, is_exists_element


# 1.定义一个测试类
@pytest.mark.run(order=2)
class TestMplogin:

    # 2.定义初始化方法
    def setup_class(self):
        # 启动浏览器
        self.driver = DriverUtils.get_mp_driver()
        # 创建号对应要调用的业务层的对象
        self.login_proxy = LoginProxy()

    # 3.定义业务测试方法
    def test_mp_login(self):
        # a.定义测试数据
        phone_num = "13911111111"
        code = "246810"
        # b.调用业务层已经封装好的业务方法
        self.login_proxy.test_login(phone_num, code)
        # c.都一侧是覅结果进行断言
        assert is_exists_element(self.driver, "传智播客")

    # 4.定义一个销毁方法
    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mp_driver()
