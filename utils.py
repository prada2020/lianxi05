import json
import appium.webdriver
import selenium.webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# 公用的读取json文件数据的方法
def build_data(file_path):
    case_data = []
    # 1.打开测试数据文件
    with open(file_path, encoding="utf-8") as f:
        # 2.读取json数据
        data = json.load(f)
        # 3.遍历键值
        for test_data in data.values():
            # 4.第一层遍历键值还是对象，需要以列表的形式一次性再次获取其键值，并且追加到最终数据的列表中
            case_data.append(list(test_data.values()))
    return case_data

# 公用选择项的方法
def select_option(driver, channel_name, option_name):
    # 点击频道控件
    css_string = "[placeholder*='{}']".format(channel_name)
    driver.find_element_by_css_selector(css_string).click()
    # 获取所有频道的选项
    option_list = driver.find_elements_by_css_selector(".el-select-dropdown__item span")
    # 是否找到标识
    is_element = False
    # 遍历选项文本并和目标选项进行对比
    for option_element in option_list:
        # 如果相等则做点击事件
        if option_element.text == option_name:
            option_element.click()
            is_element = True
            break
        # 如果不相等则鼠标悬浮到改选项并且按向下按键
        else:
            ActionChains(driver).move_to_element(option_element).send_keys(Keys.DOWN).perform()
            is_element = False
    # 如果最后都没有找到相等的选项则提示没有该频道
    if is_element is False:
        NoSuchElementException("can't find {} option".format(option_name))


# 根据文本判断元素是否存在的公用方法
def is_exists_element(driver, text):
    """
    :param driver:浏览器驱动对象
    :param text: 要查找的文本的局部信息
    :return:
    """
    # 定义要查找的元素xpath表达式
    xpath_string = "//*[contains(text(), '{}')]".format(text)
    try:
        # 尝试去查找指定的元素，如找到了则直接赋值给is_suc
        is_suc = driver.find_element_by_xpath(xpath_string)
    except Exception as e:
        # 如果没有找到元素的异常
        is_suc = False
        # 同时抛出找不到元素的异常
        NoSuchElementException("no find text is {} element".format(text))
    # 返回is_suc的值
    return is_suc


# 根据元素的属性值信息来判断元素是否存在
def is_exists_element_by_attr(driver, attr_name, attr_value):
    # 定义查找元素的表达式
    xpath_string = "//*[contains(@{}, '{}')]".format(attr_name, attr_value)
    try:
        # 尝试去查找指定的元素，如找到了则直接赋值给is_suc
        is_suc = driver.find_element_by_xpath(xpath_string)
    except Exception as e:
        # 如果没有找到元素的异常
        is_suc = False
        # 同时抛出找不到元素的异常
        NoSuchElementException("no find element")
    # 返回is_suc的值
    return is_suc


class DriverUtils:

    # 自媒体驱动对象的私有属性
    __mp_driver = None
    # 后台管理系统驱动对象的私有属性
    __mis_driver = None
    # app驱动对象的私有属性
    __app_driver = None
    # MP 自媒体开关
    __mp_key = True

    # MIS后台管理系统的开关
    __mis_key = True

    # 自媒体
    @classmethod
    def get_mp_driver(cls):
        if cls.__mp_driver is None:
            cls.__mp_driver = selenium.webdriver.Chrome()
            cls.__mp_driver.maximize_window()
            cls.__mp_driver.implicitly_wait(30)
            cls.__mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls.__mp_driver

    # 修改mp开关的方法
    @classmethod
    def quit_mp_driver(cls):
        if cls.__mp_driver is not None and cls.__mp_key:
            cls.__mp_driver.quit()
            cls.__mp_driver = None

    @classmethod
    def change_mp_key(cls, key):
        cls.__mp_key = key

    # 后台管理系统
    @classmethod
    def get_mis_driver(cls):
        if cls.__mis_driver is None:
            cls.__mis_driver = selenium.webdriver.Chrome()
            cls.__mis_driver.maximize_window()
            cls.__mis_driver.implicitly_wait(30)
            cls.__mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls.__mis_driver

    @classmethod
    def quit_mis_driver(cls):
        if cls.__mis_driver is not None and cls.__mis_key:
            cls.__mis_driver.quit()
            cls.__mis_driver = None

    @classmethod
    def change_mis_key(cls, key):
        cls.__mis_key = key

    # app
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            # 手机端连接配置
            cap = {
                "platformName": "Android",
                "deviceName": "emulator",
                "appPackage": "com.itcast.toutiaoApp",
                "appActivity": ".MainActivity",
                "noReset": True
            }

            # 创建驱动对象
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
            cls.__app_driver.implicitly_wait(30)
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver is not None:
            cls.__app_driver.quit()
            cls.__app_driver = None
