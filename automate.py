from selenium import webdriver
import time

chrome_path = r"C:\Users\giril\AppData\Local\Programs\Python\Python36-32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://web.whatsapp.com/")
time.sleep(15);

number = int(input("Enter the number of personal chats/groups you would want to message "))

for num in range(number):
    name = input("Enter name to whom u want to send a message ")
    
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/button').click()
    time.sleep(2)
    
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]').send_keys(name)
    time.sleep(2)
    
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div').click()
    time.sleep(1)
    
    done = 1
    while done:
        message = input("Enter the message you want to enter ")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(message)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()
        print("Would you want to send another message to the same contact ?")
        done = int(input("Enter 1 to continue, 0 to stop "))
        
print("All done")
