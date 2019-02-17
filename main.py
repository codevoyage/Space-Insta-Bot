import schedule
from functions import post_picture_insta

schedule.every().day.at("09:15").do(post_picture_insta)

while True:
    schedule.run_pending()



