class BaseAPP:

    def __init__(self, driver) -> None:
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    def click(self, locator):
        # TODO: ADD WAITER
        el = self.driver.find_element(*locator)
        el.click()

        return True

    def type_text(self, locator, text):
        # TODO: ADD WAITER
        el = self.driver.find_element(*locator)
        el.send_keys(text)

        # TODO: ADD VALIDATOR
        # if el.innerHtml != text:
        #     raise Exception(f"Text {text} was not entered into {locator} field")

        return True