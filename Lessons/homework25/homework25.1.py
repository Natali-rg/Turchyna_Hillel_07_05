from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger_homework25 import logger

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)


def login(driver):

    try:
        logger.info("Запуск браузера")

        driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

        logger.info("Відкрито сторінку QAuto")

        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Guest log in']"))).click()
        logger.info("Натиснута кнопка Sign In")

        logger.info("Логування пройшло успішно!")

    except Exception as e:
        logger.error(f"Помилка під час логування: {e}")

    finally:
        driver.quit()
        logger.info("Браузер закритий")

login(driver)


# XPath локатори

element_XPath1_Home = "//a[text()='Home']"
element_XPath2_Abput = "//button[text()='About']"
element_XPath3_Contacts = "//button[text()='Contacts']"
element_XPath4_login = "//button[text()='Guest log in']"
element_XPath5_SignIn = "//button[text()='Sign In']"
element_XPath6_QAuto = "//a[@href='/']"
element_XPath7_header_logo = "//a[@class='header_logo']"
element_XPath8_header_signin = "//button[@class='btn btn-outline-white header_signin']"
element_XPath9_header_nav = "//nav[@class='header_nav d-flex align-items-center']"
element_XPath10_header = "//header[@class='header bg-basic-dark']"
element_XPath11_headerHome = "//header//a[text()='Home']"
element_XPath12_headerAbout = "//header//button[text()='About']"
element_XPath13_Do_more = "//div[@class='hero-descriptor']//h1"
element_XPath14_Do_more_Text = "//h1[text()='Do more!']"
element_XPath15_buttonSignup = "//button[text()='Sign up']"
element_XPath16_buttonClassSignup = "//div[@class='hero-descriptor']//button"
element_XPath17_YouTube_iframe = "//iframe[@class='hero-video_frame']"
element_XPath18_aboutSection = "//div[@id='aboutSection']"
element_XPath19_contactsSection = "//div[@id='contactsSection']"
element_XPath20_fuel_expenses = "//p[text()='Log fuel expenses']"
element_XPath21_Instructions = "//p[text()='Instructions and manuals']"
element_XPath22_Title_Contacts = "//h2[text()='Contacts']"
element_XPath23_facebook = "//a[@href='https://www.facebook.com/Hillel.IT.School']"
element_XPath24_email = "//a[@href='mailto:developer@ithillel.ua']"
element_XPath25_TextFooter = "//footer//p[contains(text(),'Hillel auto developed')]"

# CSS локатори

element_CSS1_logo = "a.header_logo"
element_CSS2_navigation = ".header_nav"
element_CSS3_Home = ".header_nav a"
element_CSS4_HomeLink = ".header-link"
element_CSS5_Guest_login = ".header-link.-guest"
element_CSS6_Signin = ".header_signin"
element_CSS7_button_signin = "button.header_signin"
element_CSS8_Header = "header.bg-basic-dark"
element_CSS9_header_logo = "header .header_logo"
element_CSS10_header_buttons = "header nav button"
element_CSS11_descriptor_title = ".hero-descriptor_title"
element_CSS12_description = ".hero-descriptor_descr"
element_CSS13_button_SignUp = ".hero-descriptor_btn"
element_CSS14_video_frame = ".hero-video_frame"
element_CSS15_video_frame_YouTube = "iframe.hero-video_frame"
element_CSS16_aboutSection = "#aboutSection"
element_CSS17_contactsSection = "#contactsSection"
element_CSS18_title_aboutBlock = ".about-block_title"
element_CSS19_pictures = ".about-picture_img"
element_CSS20_buttons_socials = ".contacts_socials a"
element_CSS21_socials_link = ".socials_link"
element_CSS22_icon_facebook = ".icon-facebook"
element_CSS23_icon_telegram = ".icon-telegram"
element_CSS24_footer = ".footer"
element_CSS25_footer_logo = ".footer_logo"

