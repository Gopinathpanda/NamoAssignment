from selenium import webdriver
import time
# Script to login into gmail and send mail
# load the driver
driver = webdriver.Chrome('chromedriver.exe')



def gmail_login(email_address, password):
    """Login into gmail."""
    # to maximize window
    driver.maximize_window()

    # open the login page
    driver.get('https://stackoverflow.com/users/login')
    time.sleep(4)

    # login through Gmail credentials
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
    time.sleep(2)

    # enter the Email address
    email_field = driver.find_element_by_id('identifierId')
    email_field.clear()
    email_field.send_keys(email_address)
    time.sleep(2)

    # to click the next button
    next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/span/span')
    next.click()
    time.sleep(4)

    # enter password
    email_pass = driver.find_element_by_name("password")
    email_pass.clear()
    email_pass.send_keys(password)
    time.sleep(2)

    # to click the next button
    next_pass = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/span/span')
    next_pass.click()
    time.sleep(4)

    # load The Gmail mailbox
    driver.get("https://mail.google.com")
    time.sleep(20)

    send_mail()


def send_mail():
    """Sending mail from login mail address."""
    recipient_mail = input("Enter recipient_email:")
    body_email = input('Enter body of mail:')
    content_email = input('Enter content of mail:')

    # to click the compose mail button
    compose = driver.find_element_by_xpath('//*[@id=":kn"]/div/div')
    compose.click()
    time.sleep(4)

    # enter the recipient name
    recipient_email = driver.find_element_by_name('to')
    recipient_email.clear()
    recipient_email.send_keys(recipient_mail)
    time.sleep(2)

    # enter the subject of mail
    subject = driver.find_element_by_name('subjectbox')
    subject.clear()
    subject.send_keys(body_email)
    time.sleep(2)

    # enter the content of the mail
    content = driver.find_element_by_xpath('//*[@id=":qy"]')
    content.clear()
    content.send_keys(content_email)
    time.sleep(2)

    # for sending the mail
    send = driver.find_element_by_xpath('//*[@id=":pj"]')
    send.click()
    time.sleep(4)


email_address = input('Enter Email:')
password = input('Enter Password:')
gmail_login(email_address, password)

# quit the server
driver.quit()
