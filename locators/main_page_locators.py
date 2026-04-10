from selenium.webdriver.common.by import By

class MainPageLocators:

    # Вопросы
    important_questions_header = [By.CLASS_NAME, 'Home_SubHeader__zwi_E']
    question_1 = [By.ID, 'accordion__heading-0']
    question_2 = [By.ID, 'accordion__heading-1']
    question_3 = [By.ID, 'accordion__heading-2']
    question_4 = [By.ID, 'accordion__heading-3']
    question_5 = [By.ID, 'accordion__heading-4']
    question_6 = [By.ID, 'accordion__heading-5']
    question_7 = [By.ID, 'accordion__heading-6']
    question_8 = [By.ID, 'accordion__heading-7']

    # Ответы
    answer_1 = [By.ID, 'accordion__panel-0']
    answer_2 = [By.ID, 'accordion__panel-1']
    answer_3 = [By.ID, 'accordion__panel-2']
    answer_4 = [By.ID, 'accordion__panel-3']
    answer_5 = [By.ID, 'accordion__panel-4']
    answer_6 = [By.ID, 'accordion__panel-5']
    answer_7 = [By.ID, 'accordion__panel-6']
    answer_8 = [By.ID, 'accordion__panel-7']

    # Кнопки заказать
    order_button_top = [By.CSS_SELECTOR, '.Button_Button__ra12g']
    order_button_low = [By.CSS_SELECTOR, '.Button_Button__ra12g.Button_UltraBig__UU3Lp']

    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']