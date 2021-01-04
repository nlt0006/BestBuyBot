from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import info


url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442'

count = 1
still_working = True


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
time.sleep(3)

while still_working:

    try:
        # adds to cart
        driver.find_element_by_css_selector('button.btn-primary:nth-child(1)').click()
        print("\n Item found, adding to cart... \n")
        time.sleep(2)

        # go to the cart and then click checkout
        driver.get("https://www.bestbuy.com/cart")
        time.sleep(2)

        # checks to make sure there's only one item in the cart
        if (driver.find_element_by_class_name('cart-link').get_attribute('aria-label')) == 'Cart, 1 item':

            # proceeds to checkout
            print("\n Proceeding to checkout...\n")
            driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[1]/div[1]/section[2]/div/div/div[3]/div[1]/div[1]/button').click()
            time.sleep(4)

            # fills in login information
            print("\n Signing in...\n")
            driver.find_element_by_xpath('//*[@id="fld-e"]').send_keys(info.username)
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="fld-p1"]').send_keys(info.password)
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[3]/button').click()
            time.sleep(3)

            try:
                # fills in cvv information
                driver.find_element_by_xpath('//*[@id="credit-card-cvv"]').send_keys(info.cvv)
                time.sleep(3)
            except:
                # for some reason it wasn't always asking for my cvv, so this will skip that step if not asked for 
                pass

            # sets to break out of loop
            still_working = False

            # submits order
            print("\n Submitting order...\n")
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[3]/div/button').click()

            time.sleep(3)
            print("\n Success! \n")
        else:
            # sets to break out of loop
            still_working = False

            print("There's more than one item in your cart...\n ____EXITING PROGRAM____")


    except:
        # because some times it's just fun to see how much work the computer does when you don't have to do it
        count += 1

        print("\n Not yet available, waiting and refreshing (in 10 seconds) to try for attempt #", count)

        time.sleep(10)

        driver.refresh()
