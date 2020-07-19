from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.app.base_page import BasePage, BaseHandle
from utils import DriverUtils


# 对象库层
class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        # 频道区域
        self.channel_area = (By.XPATH, "//*[@class='android.widget.HorizontalScrollView']")
        # 频道
        self.channel_option = (By.XPATH, "//*[contains(@text, '{}')]")
        # 第一条文章信息
        self.first_artical = (By.XPATH, "//*[contains(@text, '评论')]")

    def find_channel_area(self):
        return self.find_elt(self.channel_area)

    def find_channel_option(self, channel_name):
        return self.driver.find_element(self.channel_option[0], self.channel_option[1].format(channel_name))

    def find_first_artical(self):
        return self.find_elt(self.first_artical)


# 操作层
class HomeHandle(BaseHandle):

    def __init__(self):
        super().__init__()
        self.home_page = HomePage()

    # 1.选择频道
    def check_channel_option(self, channel_name):
        # 获取区域范围
        area = self.home_page.find_channel_area()
        x = area.location["x"]
        y = area.location["y"]
        w = area.size["width"]
        h = area.size["height"]
        start_x = x + w * 0.75
        start_y = y + h * 0.5
        end_x = x + w * 0.25
        end_y = start_y

        # 在当前区域根据频道的名称来查找对应元素
        while True:
            # 获取当前页面信息
            page_old = DriverUtils.get_app_driver().page_source
            # 如果找到元素则点击
            try:
                self.home_page.find_channel_option(channel_name).click()
            # 如果没有找到则进行滑动
            except Exception as e:
                DriverUtils.get_app_driver().swipe(start_x, start_y, end_x, end_y)
                # 获取滑动之后的页面信息
                page_new = DriverUtils.get_app_driver().page_source
                # 判断滑动之前和滑动之后的页面信息是否相等
                if page_old == page_new:
                    raise NoSuchElementException("not find {} channel".format(channel_name))

    # 2.点击第一条文章信息
    def click_first_artical(self):
        self.home_page.find_first_artical().click()


# 业务层
class HomeProxy:

    def __init__(self):
        self.home_handle = HomeHandle()

    # 根据频道查询文章
    def test_query_by_chname(self, chname):
        # 1.选择频道
        self.home_handle.check_channel_option(chname)
        # 2.点击第一条文章
        self.home_handle.click_first_artical()
