import sys
import os
import keyboard, time

from selenium import webdriver
from selenium.webdriver.common.by import By

config = {
    'webdriver': f'{os.getcwd()}/chromedriver.exe',
    'base_url': 'https://zakup.sk.kz/#/ext',
    'path_token': f'{os.getcwd()}/token.txt',
    'path_ecp': f'{os.getcwd()}/GOSTKNCA_1767ac8f3a5598d8c0ff1cec24db76b63f648b6d.p12',
    'password_ecp': 'Aa123456', 'password_samruk': '2016Serik'
}


def auth_passing_process():
    keyboard.write(config['path_ecp'])
    time.sleep(0.01)
    keyboard.send('enter')

    keyboard.press('shift')
    keyboard.send('tab')
    time.sleep(0.05)
    keyboard.send('tab')
    time.sleep(0.05)
    keyboard.send('tab')
    time.sleep(0.05)
    keyboard.release('shift')
    time.sleep(0.05)
    keyboard.write(config['password_ecp'])
    time.sleep(0.05)
    keyboard.send('enter')
    time.sleep(0.01)
    keyboard.send('enter')
    time.sleep(0.01)
    keyboard.send('enter')

    control_password_system = get_control(driver, By.XPATH, '//*[@id="password"]')
    control_password_system.send_keys(config['password_samruk'])
    time.sleep(0.01)
    keyboard.send('enter')


def get_control(driver, by, value):
    control = None
    while not control:
        try:
            control = driver.find_element(by=by, value=value)
        except:
            pass

    return control


def authentication(driver):
    """authentication"""

    # ищем на кнопку Войти
    control_login = get_control(driver, By.XPATH, '/html/body/sk-app/sk-external-template/div/div[2]/div/sk-external-navbar/nav/div[1]/div[2]/span/a[1]')
    # нажимаем на кнопку Войти
    control_login.click()

    # ищем на кнопку Выбрать сертификат
    control_choice_certificate = get_control(driver, By.XPATH, '/html/body/sk-app/sk-external-template/div/div[2]/div/sk-external-navbar/nav/ngb-modal-window/div/div/jhi-login-modal/div[2]/div/div[2]/button')
    # нажимаем на кнопку Выбрать сертификат
    control_choice_certificate.click()
    time.sleep(1)
    # аутентификация
    auth_passing_process()


def get_token(driver):
    while True:
        token = driver.execute_script("return window.sessionStorage.getItem('jhi-authenticationtoken');")
        if token:
            with(open(config['path_token'], 'w', encoding='utf-8')) as file:
                file.write(token)
                return token


if __name__ == '__main__':
    driver = webdriver.Chrome(config['webdriver'])
    # driver.maximize_window()
    driver.get(config['base_url'])

    authentication(driver)

    token = get_token(driver)

    t1 = 12

    # sys.exit()





