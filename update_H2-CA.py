from selenium import webdriver
from time import sleep
from signal import signal, SIGINT
from datetime import datetime
from sys import exit

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    try:
        driver.close()
    except:
        pass
    print('browser closed')
    exit(0)

if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)
    print('Running. Press CTRL-C to exit.')

##########################################################################

driver = webdriver.Chrome('C:/Users/kenneth.schmahl/bin/chromedriver')
driver.get("https://h2-ca.com/map?reg=3")

while True:
    print('  sleeping')
    for i in range(60):
        sleep(1)
    now = datetime.now().strftime('%I:%M%p')
    print('##refreshing, %s'%now)
    driver.refresh()

##########################################################################

