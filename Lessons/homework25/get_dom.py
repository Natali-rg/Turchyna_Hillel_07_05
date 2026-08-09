
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


URL = "https://guest:welcome2qauto@qauto2.forstudy.space/"


options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    driver.get(URL)

    # Чекаємо, поки браузер завантажить сторінку
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    # Отримуємо реальний DOM
    dom = driver.execute_script(
        "return document.documentElement.outerHTML;"
    )

    # Зберігаємо DOM у файл
    with open("qauto_dom.html", "w", encoding="utf-8") as file:
        file.write(dom)

    print("DOM успішно збережено у файл qauto_dom.html")

finally:
    driver.quit()

