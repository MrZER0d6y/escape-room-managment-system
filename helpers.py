from datetime import *
from constants import *


def create_unique_room_id(rooms):
    if not rooms:
        return 1
    old_id = rooms[-1]["room_id"]
    room_id = "".join([ch for ch in old_id if ch.isdigit()])
    room_id = int(room_id) + 1
    if len(str(room_id)) == 1:
        return "R00" + str(room_id)
    if len(str(room_id)) == 2:
        return "R0" + str(room_id)
    return "R" + str(room_id)

def create_unique_booking_id(bookings):
    if not bookings:
        return 1
    old_id = bookings[-1]["booking_id"]
    booking_id = "".join([ch for ch in old_id if ch.isdigit()])
    booking_id = int(booking_id) + 1
    if len(str(booking_id)) == 1:
        return "B00" + str(booking_id)
    if len(str(booking_id)) == 2:
        return "B0" + str(booking_id)
    return "B" + str(booking_id)

def print_room(room):
    print(f"\nRoom ID: {room["room_id"]}\nName: {room["name"]}\n"
        f"Difficulty: {room["difficulty"]}\nDuration: {room["duration"]}\n"
        f"Minimum Players: {room["min_players"]}\nMaximun Players: {room["max_players"]}\n"
        f"Price Per Player: {room["price_per_player"]}\nActive: {room["is_active"]}")
    return

def print_booking(booking):
    print(f"\nBooking ID: {booking["booking_id"]}\nCustomer Name: {booking["customer_name"]}\n"
        f"Room ID: {booking["room_id"]}\nBooking Date: {booking["booking_date"]}\n"
        f"Start Time: {booking["start_time"]}\nPlayers: {booking["players"]}\n"
        f"Total Price: {booking["total_price"]}\nStatus: {booking["status"]}\n"
        f"Cancellation Fee: {booking["cancellation_fee"]}")
    return

def get_choice(options):
    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("\nChoose an option: "))
        except ValueError:
            print("\nChoise must be integer, try again.")
            continue
        if choice < 1 or choice > options:
            print("\nChoise must be positive, try again.")
            continue
        valid_choice = True
    return choice

def get_room_id(rooms):
    valid_id = False
    while not valid_id:
        try:
            room_id = int(input("\nRoom ID: "))
        except ValueError:
            print("\nRoom ID must be integer, try again.")
            continue
        if room_id < 1:
            print("\nRoom ID must be positive, try again.")
            continue
        if room_id > len(rooms):
            print("\nRoom ID does not exists, try again.")
            continue
        valid_id = True
    if len(str(room_id)) == 1:
        return "R00" + str(room_id)
    elif len(str(room_id)) == 2:
        return "R0" + str(room_id)
    return "R" + str(room_id)

def get_booking_id(bookings):
    valid_id = False
    while not valid_id:
        try:
            booking_id = int(input("\nBooking ID: "))
        except ValueError:
            print("\nBooking ID must be integer, try again.")
            continue
        if booking_id < 1:
            print("\nBooking ID must be positive, try again.")
            continue
        if booking_id > len(bookings):
            print("\nBooking ID does not exists, try again.")
            continue
        valid_id = True
    if len(str(booking_id)) == 1:
        return "B00" + str(booking_id)
    elif len(str(booking_id)) == 2:
        return "B0" + str(booking_id)
    return "B" + str(booking_id)

def get_name():
    valid_name = False
    while not valid_name:
        name = input("\nName: ").title()
        if not name:
            print("\nName cannot be empty, try again.")
            continue
        valid_name = True
    return name

def get_room_difficulty():
    valid_difficulty = False
    while not valid_difficulty:
        difficulty = input("\nDifficulty (Easy/Medium/Hard): ").lower()
        if difficulty not in ("easy", "medium", "hard"):
            print("\nDifficulty must be Easy/Medium/Hard, try again.")
            continue
        valid_difficulty = True
    return difficulty

def get_room_duration():
    valid_duration = False
    while not valid_duration:
        try:
            duration = int(input("\nDuration: "))
        except ValueError:
            print("\nDuration must be integer, try again.")
            continue
        if duration < 1 or duration > 705:
            print("\nDuration must be between 1 to 705, try again.")
            continue
        valid_duration = True
    return duration

def get_min_players():
    valid_min = False
    while not valid_min:
        try:
            min_players = int(input("\nMinimum Players: "))
        except ValueError:
            print("\nMinimum players must be integer, try again.")
            continue
        if min_players < 1:
            print("\nMinimum players must be positive, try again.")
            continue
        valid_min = True
    return min_players

def get_max_players(min_players):    
    valid_max = False
    while not valid_max:
        try:
            max_players = int(input("\nMaximum Players: "))
        except ValueError:
            print("\nMaximum players must be integer, try again.")
            continue
        if max_players < min_players:
            print("\nMaximum players must be greater than minimum players, try again.")
            continue
        valid_max = True
    return max_players

def get_price_per_player():
    valid_price = False
    while not valid_price:
        try:
            price = int(input("\nPrice Per Player: "))
        except ValueError:
            print("\nPrice per player must be integer, try again.")
            continue
        if price < 1:
            print("\nPrice per player must be positive, try again.")
            continue
        valid_price = True
    return price

def get_active_status():
    valid_status = False
    while not valid_status:
        status = input("\nRoom is active (true/false)? ")
        if status not in ("true", "false"):
            print("\nStatus must be true/false, try again.")
            continue
        valid_status = True
    return status

def room_is_active(rooms):
    is_active = False
    while not is_active:
        room_id = get_room_id(rooms)
        for room in rooms:
            if room["room_id"] == room_id:
                if room["is_active"] == True:
                    print("\nThe room is available!")
                    return room_id
                print("\nThe room is occupied, choose another room.")

def get_year(past):
    valid_year = False
    while not valid_year:
        try:
            year = int(input("\nYear: "))
        except ValueError:
            print("\nYear must be integer, try again.")
            continue
        if year < datetime.today().year and not past:
            print(f"\nYear must be {datetime.today().year} or more, try again.")
            continue
        valid_year = True
    return year

def get_month(year, past):
    valid_month = False
    while not valid_month:
        try:
            month = int(input("\nMonth: "))
        except ValueError:
            print("\nMonth must be integer, try again.")
            continue
        if month < 1 or month > 12:
            print(f"\nMonth must be between 1 to 12, try again.")
            continue
        if year == datetime.today().year and month < datetime.today().month and not past:
            print(f"\nMonth must be more than {datetime.today().month}, try again.")
            continue
        valid_month = True
    return month

def get_day(month, past):
    valid_day = False
    while not valid_day:
        try:
            day = int(input("\nDay: "))
        except ValueError:
            print("\nDay must be integer, try again.")
            continue
        if month < 1 or month > 31:
            print(f"\nDay must be between 1 to 31, try again.")
            continue
        if month == datetime.today().month and day < datetime.today().day and not past:
            print(f"\nDay must be more than {datetime.today().day}, try again.")
            continue
        valid_day = True
    return day

def get_booking_date(past=False):
    valid_date = False
    while not valid_date:
        year = get_year(past)
        month = get_month(year, past)
        day = get_day(month, past)
        try:
            datetime(year=year,month=month,day=day)
        except ValueError as error:
            print(f"Error: {error}")
            continue
        if datetime(year=year,month=month,day=day) < datetime.now() and not past:
            print("\nDate is already past, try again.")
            continue
        return f"{year}-{month}-{day}"

def get_start_time():
    valid_start_time = False
    while not valid_start_time:
        start_time = input("\nEnter the time (HH:MM): ")
        try:
            parsed_time = datetime.strptime(start_time, "%H:%M").time()
        except ValueError:
            print("\nInvalid format, Please enter time as HH:MM.")
            continue
        valid_start_time = True
    return start_time

def get_room_duration(rooms, room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            return room["duration"]

def can_book_room(rooms, room_id, date_str, time_str, bookings, update=False, booking_id=None):
    new_duration = get_room_duration(rooms, room_id)

    new_start = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    new_end = new_start + timedelta(minutes=new_duration + RESERVED_TIME)

    open_time = datetime.strptime(f"{date_str} 10:00", "%Y-%m-%d %H:%M")
    close_time = datetime.strptime(f"{date_str} 22:00", "%Y-%m-%d %H:%M")
    if new_start < open_time or new_end > close_time:
        print(f"\nThe game falls outside operating hours (10:00 - 22:00).")
        return False

    for booking in bookings:
        if booking["booking_id"] == booking_id:
            continue
        if booking["room_id"] != room_id:
            continue
        if booking["booking_date"] != date_str:
            continue
        if booking["status"] != "Active":
            continue

        existing_start = datetime.strptime(f"{booking['booking_date']} {booking['start_time']}", "%Y-%m-%d %H:%M")
        existing_end = existing_start + timedelta(minutes=new_duration + RESERVED_TIME)

        if new_start < existing_end and new_end > existing_start:
            print(f"Conflict with {booking['booking_id']} ({booking['start_time']} - {existing_end.strftime('%H:%M')}).")
            return False

    return True

def get_players(rooms, room_id):
    valid_players = False
    while not valid_players:
        try:
            players = int(input("\nPlayers: "))
        except ValueError:
            print("\nPlayers must be integer, try agin.")
            continue
        for room in rooms:
            if room["room_id"] == room_id:
                if room["min_players"] <= players and room["max_players"] >= players:
                    valid_players = True
                    continue
                print(f"\nPlayers must be between {room["min_players"]} to {room["max_players"]}, try again.")
    return players

def room_not_active(bookings, booking_id, rooms):
    for booking in bookings:
        if booking["booking_id"] == booking_id:
            for room in rooms:
                if room["room_id"] == booking["room_id"]:
                    if room["is_active"] == False:
                        return True, room["room_id"]
                    return False, room["room_id"], booking["players"]

def get_start_time_by_id(bookings, booking_id):
    for booking in bookings:
        if booking["booking_id"] == booking_id:
            return booking["start_time"]

def get_booking_date_by_id(bookings, booking_id):
    for booking in bookings:
        if booking["booking_id"] == booking_id:
            return booking["booking_date"]