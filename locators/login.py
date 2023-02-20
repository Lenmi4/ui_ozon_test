from selenium.webdriver.common.by import By
from selenium import webdriver

url = 'https://www.saucedemo.com/'


class LoginPageLocators:
    EMAIL = (By.ID, "user-name") #почта
    PASSWORD = (By.ID, "password") #пароль
    BUTTON = (By.ID, "login-button") #кнопка для авторизации после заполнения данных
    BUTTON_ACCOUNT = (By.ID, "react-burger-menu-btn") #кнопка кабинета пользователя после авторизации
    EXIT = (By.ID, "logout_sidebar_link") #выход из кабинета пользователя
    ERROR = (By.CLASS_NAME, "error-message-container") #Неверное имя пользователя или пароль



