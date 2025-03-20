from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Настройка ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Запуск в фоновом режиме без открытия окна браузера
driver = webdriver.Chrome(options=options)

def main():
    while True:
        query = input("Введите ваш запрос: ")
        try:
            driver.get(f'https://ru.wikipedia.org/wiki/{query}')
            content = driver.find_element(By.ID, 'mw-content-text').text
            print(content)

            while True:
                action = input("\nЧто вы хотите сделать? \n"
                               "(1) Листать параграфы текущей статьи\n"
                               "(2) Перейти на одну из связанных страниц\n"
                               "(3) Выйти из программы\n")

                if action == '1':
                    pass  # Добавьте реализацию листания параграфов
                elif action == '2':
                    related_links = driver.find_elements(By.CSS_SELECTOR, '#mw-content-text a')
                    for i, link in enumerate(related_links):
                        print(f"{i+1}. {link.text}")
                    index = int(input("\nНа какую страницу хотите перейти? Введите номер: "))
                    new_page_url = related_links[index - 1].get_attribute('href')
                    driver.get(new_page_url)
                    content = driver.find_element(By.ID, 'mw-content-text').text
                    print(content)
                elif action == '3':
                    print("\nСпасибо за использование! До свидания!")
                    driver.quit()
                    break
                else:
                    print("Неизвестная команда. Попробуйте еще раз.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
