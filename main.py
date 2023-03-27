from notification import Notification
from scarpe import Willhaben
import time

# Add user, join the julmie bot on telegram
# get user id
#   1) send message to bot
#   2) https://api.telegram.org/bot5755337602:AAHgyr1dbANnLRU9j2m17GxwAUND_ExLjKs/getUpdates



noti = Notification()

garten="https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz?PRICE_FROM=100&ISPRIVATE=1&sfId=96cbd2a0-64e0-43ca-a80a-012c2e398aa6&page=1&rows=30&keyword=Garten+lounge&PRICE_TO=300&searchKey=301&isNavigation=true"



noti.send_notification("HALLO NIKI, HALLO JULIAN! Ich halte meine Augen offen und gebe euch bescheid falls sich in der Rubrik:")
noti.send_notification(garten)
noti.send_notification("etwas neues tut!")
scrape = Willhaben()
last=scrape.get_latest_item(garten)
#noti.send_notification(last[0] +"   "+ last[1])
#noti.send_notification(scrape.get_latest_item_v2(garten))


while True:

    lastnew=scrape.get_latest_item(garten)

    if lastnew != last:
        last=lastnew
        #noti.send_notification(last[0] + "   " + last[1])
        noti.send_notification("Ich hab etwas interessantes für euch!:")
        noti.send_notification(scrape.get_latest_item_v2(garten))
    time.sleep(900)
