from selenium.webdriver.common.by import By


class LoginPageLocators:
    MODAL_WINDOW_CLOSE = (By.CSS_SELECTOR, "div[data-qa='closeAutodetectRegion']")
    SIGN_IN = (By.CLASS_NAME, "icon--account")
    EMAIL = (By.CSS_SELECTOR, "input[data-qa='loginEmail']")
    PASSWORD = (By.CSS_SELECTOR, "input[data-qa='loginPassword']")
    BUTTON = (By.CSS_SELECTOR, "button[data-qa='loginSubmit']")
    ACCOUNT = (By.CSS_SELECTOR, "span[data-qa='account-link']")
