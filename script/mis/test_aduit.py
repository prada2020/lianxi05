import time
import pytest
from config import PUB_ARTICAL_TITLE
from page.mis.aduit_page import AduitProxy
from page.mis.home_page import HomeProxy
from utils import DriverUtils, is_exists_element


# 定义测试类
@pytest.mark.run(order=102)
class TestAduit:

    # 定义初始化方法
    def setup_class(self):
        self.driver = DriverUtils()
        # 创建的业务方法所在类的对象
        self.home_proxy = HomeProxy()
        self.aduit_proxy = AduitProxy()

    # 3.定义测试方法：文案的测试步骤----业务中的业务方法
    def test_aduit_artical(self):
        # 定义测试数据
        ar_title = PUB_ARTICAL_TITLE
        # 执行测试步骤
        self.home_proxy.to_aduit_page()
        self.aduit_proxy.test_aduit_ar(ar_title)
        time.sleep(5)
        # 断言
        assert is_exists_element(self.driver, PUB_ARTICAL_TITLE)

    # 4.定义销毁方法
    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mis_driver()

