import schedule
from functions import post_picture_insta

schedule.every().day.at("11:10").do(post_picture_insta)

while True:
    schedule.run_pending()
