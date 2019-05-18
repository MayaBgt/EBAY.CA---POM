class HomePage():

    def __init__(self, driver):

        self.driver = driver
        self.signin_link_xpath = "//a[contains(text(),'Sign in')]"
        self.click_deals_xpath = "//a[@class='gh-p']"
        self.name_link_xpath = "//b[@class='gh-eb-arw gh-sprRetina']"
        self.signout_link_xpath = "//a[contains(text(),'Sign out')]"


    def click_signin(self):
        self.driver.find_element_by_xpath(self.signin_link_xpath).click()


    def click_deals(self):
        self.driver.find_element_by_xpath(self.click_deals_xpath).click()


    def signout(self):

        self.driver.find_element_by_xpath(self.name_link_xpath).click()
        self.driver.find_element_by_xpath(self.signout_link_xpath).click()
