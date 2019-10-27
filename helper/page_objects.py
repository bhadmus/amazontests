from values import strings



class Guest:

    def __init__(self,driver):
        self.driver = driver

    def guest_journey(self):
        # search an item
        self.driver.browse.find_element_by_id(strings.search_box).send_keys(strings.search_item)
        self.driver.browse.find_element_by_css_selector(strings.search_button).click()

        # select an item
        self.driver.browse.find_element_by_xpath(strings.select_item).click()
        self.driver.browse.implicitly_wait(10)

        # add iem to basket
        self.driver.browse.find_element_by_id(strings.add_to_basket).click()
        self.driver.browse.implicitly_wait(10)
        # proceed to checkout
        self.driver.browse.find_element_by_id(strings.checkout).click()
        self.driver.browse.implicitly_wait(10)
