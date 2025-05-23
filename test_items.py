import time
import pytest
from selenium.webdriver.common.by import By


def test_is_button_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.")
    time.sleep(15)
    button = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button')
    if button.text == "Ajouter au panier":
        print("Button text is correct")
    assert button.is_displayed(), 'Кнопка не найдена'


