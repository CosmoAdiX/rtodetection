from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def get_vehicle_details(license_number):
    # Configure WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run browser in headless mode (optional)
    chrome_service = Service('path/to/chromedriver')  # Update this path
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        # Open the website
        driver.get('https://vahan.parivahan.gov.in/nrservices/faces/user/citizen/searchstatus.xhtml')  # Replace with the actual URL

        # Locate the search input field and submit button
        search_box = driver.find_element(By.ID, 'regn_no1_exact')  # Update this selector
        search_box.send_keys(license_number)
        
        # Submit the form or click the search button
        submit_button = driver.find_element(By.ID, 'j_idt39')  # Update this selector
        submit_button.click()
        
        # Wait for results to load
        time.sleep(5)  # Adjust this if needed
        
        # Extract vehicle details
        details = driver.find_element(By.ID, 'details-section').text  # Update this selector
        return details

    except Exception as e:
        return f"An error occurred: {e}"

    finally:
        driver.quit()

if __name__ == "__main__":
    license_number = input("Enter vehicle license number: ")
    details = get_vehicle_details(license_number)
    print("Vehicle Details:")
    print(details)
