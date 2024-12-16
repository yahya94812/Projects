from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the website
    driver.get("https://pda-results.contineo.in/index.php")
    # Find the input element by its ID
    elem = driver.find_element(By.ID, "usn")
    # Clear the input field and enter the USN
    elem.clear()

    elem.send_keys("3PD23CS001")
    # Submit the form by pressing Enter
    elem.send_keys(Keys.RETURN)


    with open('pda_results.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        #writer.writerow(['USN','Name','Section', 'SGPA'])

    for i in range(1,188):
        if i<10:
            usn="3PD23CS00"+str(i)
            sec='A'
        elif i<100:
            usn="3PD23CS0"+str(i)
            if i<63:
                sec='A'
            else:
                sec='B'    
        else:
            usn="3PD23CS"+str(i)
            if i<125:
                sec='B'
            else:
                sec='c'  

        print(usn)
        # Execute the JavaScript code to open the new page
        submitstr = f"submitfrom('{usn}', '7');"
        driver.execute_script(submitstr)
        time.sleep(3)

        # Extract the SGPA from the new page
        sgpa_element = driver.find_element(By.XPATH, "//div[@class='uk-card uk-card-default uk-card-body credits-sec3']/p")
        sgpa= sgpa_element.text

        # Extract name
        name_element = driver.find_element(By.XPATH, '//h3[@style="font-size:14pt;"]')
        name = name_element.text

        # Write the SGPA value to a CSV file
        with open('pda_results.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([usn, name, sec, sgpa])

        driver.execute_script("history.back();")    

finally:
    # Close the browser
    driver.close()
