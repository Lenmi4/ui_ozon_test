from selenium.webdriver.common.by import By
from selenium import webdriver

url = 'https://www.gloria-jeans.ru/'


class LoginPageLocators:
    MODAL_WINDOW_CLOSE = (By.CSS_SELECTOR, "div[data-qa='closeAutodetectRegion']") #закрыть высплывающее окно
    SIGN_IN = (By.CSS_SELECTOR, "span[data-qa='account-link']") #кнопка авторизации
    EMAIL = (By.CSS_SELECTOR, "input[data-qa='loginEmail']") #почта
    PASSWORD = (By.CSS_SELECTOR, "input[data-qa='loginPassword']") #пароль
    BUTTON = (By.CSS_SELECTOR, "button[data-qa='loginSubmit']") #кнопка для авторизации после заполнения данных
    FORM = (By.CLASS_NAME, "page-newhomepage")  # страница после авторизации пользователя
    ACCOUNT = (By.CSS_SELECTOR, "span[data-qa='account-link']") #кнопка кабинета пользователя после авторизации
    EXIT = (By.CLASS_NAME, "modal-account-choice caption--red") #выход из кабинета пользователя
    EMAIL_ERROR = (By.XPATH, "/html/body/div[16]/div/div[1]/div[3]/div[1]/div[2]/form/p[2]") #Неверное имя пользователя или пароль


