from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


logging.basicConfig(filename='test_run.txt',
                    filemode='a+', format='%(created)f - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )

url='https://www.amazon.com/'

def get_driver():
    try:
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        
    except Exception as error:
        raise Exception(error)


driver=get_driver()

def go_to_page(driver,url, new_window=False):
    try:
        if new_window:
            driver.execute_script(f"window.open('{url}');")
        else:
            driver.get(url)
            driver.maximize_window()
    except Exception as e:
        logging(e)
        


def find_and_send_keys(driver,loc, inp_text, timeout=3):
    try:
        elem = find(driver,loc, timeout)
        elem.send_keys(inp_text)
        
    except Exception as e:
        logging(e)
def find(driver,loc, timeout=3, get_text="", get_attribute=""):
    try:
        elem = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located(loc))
        logging("The element was successfully presented")  
        if get_text:
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem         
    except Exception as e:
        logging(e)

def find_elem(driver, loc, sec=10):
    elem = WebDriverWait(driver, sec).until(
        EC.presence_of_element_located(loc))
    return elem
def find_all(driver,loc, timeout=10):
    try:
        elements = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_all_elements_located(loc),
                                                        message=f"Elements '{loc}' not found!")
    except Exception as e:
        logging(e)
        return False
    return elements

search_field=(By.XPATH,"//input[@id='twotabsearchtextbox']")
search_results=(By.XPATH,"//img[@class='s-image']")
#submit=(By.XPATH,"input[id='nav-search-submit-button']")

def searching(get_driver):

    
    find_and_send_keys(get_driver, search_field, 'Automation')
    find_elem(get_driver, search_field).send_keys(Keys.ENTER)
    find(search_field)
    find_and_send_keys(get_driver,search_field,"present for kids")
    find_elem(get_driver,search_field).send_keys(Keys.ENTER)
    res=find_all(search_results)
    return len(res)

