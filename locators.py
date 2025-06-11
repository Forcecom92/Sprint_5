from selenium.webdriver.common.by import By

class BurgerLocators:
    BUTTON_ACCOUNT = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]") # кнопка личный кабинет
    BUTTON_REGISTRATION = (By.XPATH, "//*[contains(@href, '/register')]") # кнопка Зарегистрироваться
    BUTTON_ENTER_MAIN = (By.XPATH, "//button[text()= 'Войти']") # кнопка Войти после заполнения полей почта и пароль
    BUTTON_FORGOT_PASSWORD = (By.XPATH, "//*[contains(@href, '/forgot-password')]") # кнопка восстановить пароль
    BUTTON_FINAL_REGISTRATION = (By.XPATH, "//button[text()= 'Зарегистрироваться']") # кнопка Зарегистрироваться после ввода данных
    BUTTON_ENTER = (By.XPATH, "//*[contains(@class, 'Auth_link__1fOlj')]") # кнопка Войти после "Уже зарегистрированы?"
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()= 'Войти в аккаунт']") # кнопка Войти в аккаунт
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']") #кнопка конструктор
    BUTTON_EXIT = (By.XPATH, "//button[text()= 'Выход']") # кнопка Выход

    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    FORM_AN_ORDER = (By.XPATH, "//button[text()= 'Оформить заказ']") # кнопка Оформить заказ
    TITLE_PROFILE = (By.XPATH, "//*[contains (@href, '/account/profile')]") # кнопка Профиль
    TITLE_COLLECT_BURGER = (By.XPATH, "//h1[text() = 'Соберите бургер']") # заголовок Соберите бургер

    WRONG_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']") # надпись Некорректный пароль
    TITLE_ENTER = (By.XPATH, "//h2[text()='Вход']") # форма с надписью вход для ввода почты и пароля
    INPUT_NAME = (By.XPATH, "//label[text() = 'Имя']/../input") # ввод имени при регистрации
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input") # ввод почты при регистрации
    INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/../input") # ввод пароля при регистрации

    SAUCE_UNFOCUSED = (By.XPATH, "//span[text()='Соусы']//parent::div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    SAUCE_IN_FOCUS = (By.XPATH,"//span[text()='Соусы']//parent::div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    TOPPING_UNFOCUSED = (By.XPATH, "//span[text()='Начинки']//parent::div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    TOPPING_IN_FOCUS = (By.XPATH,"//span[text()='Начинки']//parent::div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    BREAD_UNFOCUSED = (By.XPATH, "//span[text()='Булки']//parent::div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    BREAD_IN_FOCUS = (By.XPATH,"//span[text()='Булки']//parent::div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
