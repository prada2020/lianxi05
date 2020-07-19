import logging
import time
import pytest

from config import PUB_ARTICAL_TITLE, BASE_PATH
from page.mp.home_page import HomeProxy
from page.mp.publish_artical_page import PubArProxy
from utils import DriverUtils, is_exists_element, build_data


# 1.定义测试类
@pytest.mark.run(order=3)
class TestPubArtical:

    # 2.定义初始化方法
    def setup_class(self):
        self.driver = DriverUtils.get_mp_driver()
        self.home_proxy = HomeProxy()
        self.pub_ar_proxy = PubArProxy()

    # 3.定义测试方法
    @pytest.mark.parametrize("ar_cont, ch_name", build_data(BASE_PATH + "/data/test_pub_artical_data.json"))
    def test_pub_artical(self, ar_cont, ch_name):

        # 定义测试数据
        ar_title = PUB_ARTICAL_TITLE
        # ar_content = "我要去找工作"
        # option_name = "数码产品"
        logging.info("发布文章信息为文章标题={}， 文章内容={}， 文章频道={}".format(ar_title, ar_cont, ch_name))
        # 调用业务层方法
        logging.info("------>调用首页进入发布文章的业务方法")
        self.home_proxy.to_pub_pg()
        logging.info("------>调用发布文章页面发布文章的业务方法")
        # self.pub_ar_proxy.test_pup_artical(ar_title, ar_content, option_name)
        self.pub_ar_proxy.test_pup_artical(ar_title, ar_cont, ch_name)
        # 执行断言
        is_exists_element(self.driver, "新增文章成功")

    # 4.定义销毁方法
    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mp_driver()