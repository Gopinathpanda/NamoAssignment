# NamoAssignment
This is about login into gmail and send mail after login using python script

1. Install these tools
    * Python
    * Selenium(pip install selenium)

1. Download chromedriver and extract(https://chromedriver.chromium.org/downloads)

1. Detail Process

    * Some websites, like stackoverflow.com allow you to sign in to their services using "Sign in with Google" it must happen via Google OAuth 2.0 authentication.
    * Open a new browser window that is controlled by selenium webdriver
    * In the same window load the StackOverflow login page (or any other site that uses "Sign in with Google")
    * Choose for "Log in with Google"
    * Provide your Google account credentials and login to StackOverflow
    * Load the Google mailbox by opening https://mail.google.com/ or https://www.gmail.com/
    * Open the compose mail
    * Provide recipient mail, body and content.
    * Close the webdriver

