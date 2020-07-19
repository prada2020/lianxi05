"""发布文章页面"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.mp.base_page import BasePage, BaseHandle
from utils import DriverUtils, select_option


# 对象库层：将所有测试用例所需要在该界面操作的元素全部定义对应的实例方法找回来
class PubArPage(BasePage):

    # 在初始化方法中定义元素的实例属性，并且赋值，值为定位方式以及定位方式的值
    def __init__(self):
        super().__init__()
        # 文章标题
        self.ar_title = (By.CSS_SELECTOR, "[placeholder*='文章名称']")
        # iframe
        self.cont_iframe = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        # 文章内容
        self.ar_content = (By.CSS_SELECTOR, "body")
        # 封面
        self.ar_cover = (By.XPATH, "//*[text()='自动']")
        # 频道
        self.channel = (By.CSS_SELECTOR, "[placeholder*='请选择']")
        # 频道选项
        self.channel_option = (By.XPATH, "//*[text()='上海项目']")
        # 发表
        self.pub_btn = (By.XPATH, "//*[text()='发表']")

    def find_ar_title(self):
        return self.find_elt(self.ar_title)

    def find_cont_iframe(self):
        return self.find_elt(self.cont_iframe)

    def find_ar_content(self):
        return self.find_elt(self.ar_content)

    def find_ar_cover(self):
        return self.find_elt(self.ar_cover)

    def find_channel(self):
        return self.find_elt(self.channel)

    def find_channel_op(self):
        return self.find_elt(self.channel_option)

    def find_pub_btn(self):
        return self.find_elt(self.pub_btn)


# 操作层：通过调用对象库层的实例化方法拿到元素对象，定义对应操作方法
class PubArHandle(BaseHandle):

    def __init__(self):
        self.pubar_page = PubArPage()

    # 输入文章标题
    def input_ar_title(self, title):
        self.input_text(self.pubar_page.find_ar_title(), title)

    # 输入文章内容
    def input_ar_content(self, cont):
        # iframe切换
        DriverUtils.get_mp_driver().switch_to_frame(self.pubar_page.find_cont_iframe())
        self.input_text(self.pubar_page.find_ar_content(), cont)
        # 返回默认界面
        DriverUtils.get_mp_driver().switch_to_default_content()

    # 选择封面
    def check_cover(self):
        self.pubar_page.find_ar_cover().click()

    # 选择频道
    def check_target_channel(self, option_name):
        select_option(DriverUtils.get_mp_driver(), "请选择", option_name)

    # 点击发表
    def click_pub_btn(self):
        self.pubar_page.find_pub_btn().click()


# 业务层：调用多个操作层的实例化方法可以组织成对应的业务操作
class PubArProxy:

    def __init__(self):
        self.pubar_handle = PubArHandle()

    # 发表文章
    def test_pup_artical(self, title, cont, option_name):
        # 1.输入标题
        self.pubar_handle.input_ar_title(title)
        # 2.输入文章内容
        self.pubar_handle.input_ar_content(cont)
        # 3.选择封面
        self.pubar_handle.check_cover()
        # 4.选择频道
        self.pubar_handle.check_target_channel(option_name)
        # 5.点击发表
        self.pubar_handle.click_pub_btn()
