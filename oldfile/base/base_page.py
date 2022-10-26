class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def locator(self, loc):
        return self.driver.find_element(*loc)

    def input(self, loc, text):
        self.locator(loc).send_keys(text)

    def click(self, loc):
        self.locator(loc).click()
