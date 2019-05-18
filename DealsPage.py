class DealsPage():

    def __init__(self, driver):

        self.driver = driver
        self.click_product_xpath = "//span[@class='ebayui-ellipsis-3']"



    def click_product(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.click_product_xpath).click()