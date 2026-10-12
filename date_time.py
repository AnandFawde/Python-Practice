import datetime

# instant = datetime.datetime.now()

# instant = instant.strftime("%d-%m-%Y  %H:%M:%S")
# print(instant)

target_datetime = datetime.datetime(2018,7,11,5,8,12)

current_datetime = datetime.datetime.now()

if current_datetime > target_datetime:
    print("Date has passed")

else :
    print("Date has yet to pass")