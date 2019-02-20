import schedule
from functions import start

schedule.every().day.at("09:15").do(start)

while True:
    schedule.run_pending()


