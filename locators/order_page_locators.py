from selenium.webdriver.common.by import By

class OrderPageLocators:

    first_name = [By.XPATH, "//input[@placeholder='* Имя']"]
    last_name = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_to_deliver_order = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    telephone = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    
    metro_input = [By.CSS_SELECTOR, ".select-search__input"]
    metro_dropdown = [By.CSS_SELECTOR, ".select-search__select"]
    metro_options = [By.CSS_SELECTOR, ".select-search__row"]
    
    button_next = [By.XPATH, "//button[text()='Далее']"]
    

    rental_header = [By.CLASS_NAME, 'Order_Header__BZXOb']

    date = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    header_page = [By.CLASS_NAME, 'Order_Header__BZXOb']

    date_field = [By.CSS_SELECTOR, ".Input_Input__1iN_Z.Input_Responsible__1jDKN"]

    rental_dropdown = [By.CSS_SELECTOR, ".Dropdown-control"]

    rental_option = [By.CSS_SELECTOR, ".Dropdown-option"]

    rental_periods = {
        "сутки": (By.XPATH, "//div[text()='сутки']"),
        "двое суток": (By.XPATH, "//div[text()='двое суток']"),
        "трое суток": (By.XPATH, "//div[text()='трое суток']"),
        "четверо суток":(By.XPATH, "//div[text()='четверо суток']"),
        "пятеро суток":(By.XPATH, "//div[text()='пятеро суток']"),
        "шестеро суток":(By.XPATH, "//div[text()='шестеро суток']"),
        "семеро суток":(By.XPATH, "//div[text()='семеро суток']") }

    # Чёрный жемчуг
    color_black = [By.ID, "black"]
    # Серая безысходность
    color_grey = [By.ID, "grey"]

    comment_for_courier = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

    order_button = [By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']"]

    modal_header = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]

    confirm_yes_button = [By.XPATH, "//div[@class='Order_Modal__YZ-d3']//button[text()='Да']"]

    success_modal = [By.CSS_SELECTOR, ".Order_Modal__YZ-d3"]

    success_title = [By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ"]

    view_status_button = [By.XPATH, "//button[text()='Посмотреть статус']"]

    order_number_text = [By.CSS_SELECTOR, ".Order_Text__2broi"]

