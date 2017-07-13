from behave import *
from selenium import webdriver

def before_feature(context, feature):
    context.driver = webdriver.Chrome('C:\Python27\Scripts\chromedriver.exe')
    context.driver.implicitly_wait(30)
    context.driver.maximize_window()

def after_feature(context, feature):
    context.driver.quit()
