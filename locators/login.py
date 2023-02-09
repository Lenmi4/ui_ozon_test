from selenium.webdriver.common.by import By
from selenium import webdriver

url = 'https://www.saucedemo.com/'


class LoginPageLocators:
    #MODAL_WINDOW_CLOSE = (By.CSS_SELECTOR, "div[data-qa='closeAutodetectRegion']") #закрыть высплывающее окно
    #SIGN_IN = (By.CSS_SELECTOR, "span[data-qa='account-link']") #кнопка авторизации
    EMAIL = (By.ID, "user-name") #почта
    PASSWORD = (By.ID, "password") #пароль
    BUTTON = (By.ID, "login-button") #кнопка для авторизации после заполнения данных
    #FORM = (By.CLASS_NAME, "page-newhomepage")  # страница после авторизации пользователя
    BUTTON_ACCOUNT = (By.ID, "react-burger-menu-btn") #кнопка кабинета пользователя после авторизации
    EXIT = (By.ID, "logout_sidebar_link") #выход из кабинета пользователя
    ERROR = (By.CLASS_NAME, "error-message-container") #Неверное имя пользователя или пароль


