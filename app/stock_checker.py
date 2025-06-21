from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

PINCODE_SET = False

def check_product_availability(base_url, products_list, pincode):
    global PINCODE_SET
    results = []
    options = Options()
    options.headless = True  # Run in headless mode
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    for product in products_list:
        product_url = base_url + product
        print(f"Checking availability for: {product_url}")
        driver.get(product_url)
        print(f"Page title: {driver.title}")
        time.sleep(10)  # Wait for the page to load completely
        try:
            if not PINCODE_SET:
                print("Pincode not set, entering pincode...")
                PINCODE_SET = True
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "search"))
                )
                print("Pincode popup detected")
                time.sleep(5)
                pincode_input = driver.find_element(By.ID, "search")
                pincode_input.send_keys(pincode)
                time.sleep(3)  # Wait for dropdown to populate
                dropdown_items = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.ID, "automatic"))
                )
                print(f"Found {len(dropdown_items)} dropdown items")
                for item in dropdown_items:
                    button_item = item.find_element(By.CSS_SELECTOR, ".searchitem-name")
                    print("Clicking on item:", button_item.text)
                    button_item.click()
                    time.sleep(10)  # Wait for the page to load after clicking
        except Exception as e:
            print(f"Error while entering pincode: {e}")
            raise Exception(f"Error while entering pincode: {e}")
        try:
            product_name = driver.find_element(By.CLASS_NAME, "product-name").text
        except Exception as e:
            print(f"Error finding product name: {e}")
            raise Exception(f"Error finding product name: {e}")
        try:
            print("Waiting for product availability check...")
            sold_out_box = driver.find_element(By.CLASS_NAME, "alert-danger")
            if "Sold Out" in sold_out_box.text:
                print("Product is sold out")
            else:
                print("No sold out message found, maybe product is available check manually")
        except NoSuchElementException as e:
            print(f"Product {product_name} is available Hurray! Hurry up and buy it now!")
            results.append(product_name)
        except Exception as e:
            print(f"Error checking product availability: {e}")
            raise Exception(f"Error checking product availability: {e}")
        print(f"Finished checking {product_name}, waiting for 5 seconds before next check...")
        time.sleep(5)

    return results