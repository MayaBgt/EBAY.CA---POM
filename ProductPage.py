class ProductPage():

    def __init__(self, driver):

        self.driver = driver
        self.addtocart_xpath = "//a[@id='isCartBtn_btn']"
        self.addplan_xpath = "//button[contains(text(),'Add plan')]"


    def click_addtocart(self):

        self.driver.find_element_by_xpath(self.addtocart_xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.addplan_xpath).click()

