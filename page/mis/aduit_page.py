"""
审核文章
"""
import pytest
from selenium.webdriver.common.by import By
from base.mis.base_page import BasePage, BaseHandle
from utils import select_option, DriverUtils


# 对象库层
@pytest.mark.run(order=102)
class AduitPage(BasePage):

    def __init__(self):
        super().__init__()
        # 文章名称输入框
        self.ar_title = (By.CSS_SELECTOR, "[placeholder*='文章']")
        # 查询按钮
        self.query_btn = (By.CSS_SELECTOR, ".find")
        # 通过按钮
        self.pass_btn = (By.XPATH, "//*[text() = '通过']")
        # 确认按钮
        self.confirm_btn = (By.CSS_SELECTOR, ".el-button--primary")

    def find_ar_title(self):
        return self.find_elt(self.ar_title)

    def find_query_btn(self):
        return self.find_elt(self.query_btn)

    def find_pass_btn(self):
        return self.find_elt(self.pass_btn)

    def find_cofiem_btn(self):
        return self.find_elt(self.confirm_btn)


# 操作层
class AduitHandle(BaseHandle):

    def __init__(self):
        super().__init__()
        self.aduit_page = AduitPage()

    # 文章名称输入
    def input_ar_title(self, title):
        self.input_text(self.aduit_page.find_ar_title(), title)

    # 选择文章状态
    def check_ar_status(self, status):
        select_option(DriverUtils.get_mis_driver(), "请选择", status)

    # 搜索按钮点击
    def click_query_btn(self):
        self.aduit_page.find_query_btn().click()

    # 通过按钮点击
    def click_pass_btn(self):
        self.aduit_page.find_pass_btn().click()

    # 确定按钮点击
    def click_confirm_btn(self):
        self.aduit_page.find_cofiem_btn().click()


# 业务层
class AduitProxy:

    def __init__(self):
        self.aduit_handle = AduitHandle()

    def test_aduit_ar(self, title):
        # 1.输入文章标题
        self.aduit_handle.input_ar_title(title)
        # 2.选择待审核状态
        self.aduit_handle.check_ar_status("待审核")
        # 3.点击查询
        self.aduit_handle.click_query_btn()
        # 4.点击通过按钮
        self.aduit_handle.click_pass_btn()
        # 5.点击确认按钮
        self.aduit_handle.click_confirm_btn()
        # 6.选择审核通过状态
        self.aduit_handle.check_ar_status("审核通过")
        # 7.点击查询按钮
        self.aduit_handle.click_query_btn()