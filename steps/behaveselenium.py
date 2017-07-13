from PageElements import PageElements
import time

@given('auto1 homepage is opened in browser')
def step_impl(context):
    base_url = "https://www.auto1.com/en/our-cars"
    context.driver.get(base_url)

@then('check the title of the page')
def step_impl(context):
    assert "Our cars" in context.driver.title

@when('the bmw checkbox is clicked')
def step_impl(context):
    page = PageElements(context.driver)
    page.bmw_filter.click()
    time.sleep(20)

@then('the bmw filter appears selected')
def step_impl(context):
    page = PageElements(context.driver)
    assert "checked" in page.bmw_filter.get_attribute("class")

@then('only bmw cars are displayed in list')
def step_impl(context):
    page = PageElements(context.driver)
    cars = page.cars
    for i in range(1, len(cars)):
            car_names = context.driver.find_element_by_xpath("//*[@id='car-list']/li[%s]/div[1]" % i).get_attribute('innerHTML')
            assert "BMW" in car_names

@then('each car in list has images')
def step_impl(context):
    page = PageElements(context.driver)
    cars = page.cars
    for i in range(1, len(cars)):
            car_images = context.driver.find_element_by_xpath("//*[@id='car-list']/li[%s]/div[2]/img" % i).get_attribute('src')
            assert "img-pa.auto1.com" in car_images

@then('each car in list has complete information')
def step_impl(context):
    page = PageElements(context.driver)
    cars = page.cars
    for i in range(1, len(cars)):
            for j in range(1, 7):
                car_info_table = context.driver.find_element_by_xpath("//*[@id='car-list']/li[%s]/div[3]/table/tbody/tr[%s]/td[2]" % (i,j)).get_attribute('innerHTML')
                assert car_info_table != ""
