from helpers import *
from json_handler import *

def total_active_bookings(bookings):
    if not bookings:
        print("\nThere are no bookings in the system.")
        return False
    
    print(f"\n--------- ALL ACTIVE BOOKINGS ---------")
    counter = 0
    for booking in bookings:
        if booking["status"] == "Active":
            print_booking(booking)
            counter += 1
    
    if counter == 0:
        print("\nNo active bookings found.")
        return False

    print(f"\n{counter} active bookings.")
    return True

def total_cancelled_bookings(bookings):
    if not bookings:
        print("\nThere are no bookings in the system.")
        return False
    
    print(f"\n--------- ALL CANCELLED BOOKINGS ---------")
    counter = 0
    for booking in bookings:
        if booking["status"] == "Cancelled":
            print_booking(booking)
            counter += 1
    
    if counter == 0:
        print("\nNo cancelled bookings found.")
        return False

    print(f"\n{counter} cancelled bookings.")
    return True

def total_revenue(bookings):
    if not bookings:
        print("\nThere are no bookings in the system.")
        return False
    
    print(f"\n--------- TOTAL REVENUE ---------")
    total = 0
    for booking in bookings:
        if booking["status"] == "Active":
            total += booking["total_price"]
    
    print(f"\n Total revenue: {total}.")
    return True

def total_cancellation_fees(bookings):
    if not bookings:
        print("\nThere are no bookings in the system.")
        return False
    
    print(f"\n--------- TOTAL CANCELLATION FEES ---------")
    total = 0
    for booking in bookings:
        if booking["cancellation_fee"] != 0.0:
            total += booking["cancellation_fee"]
    
    print(f"\n Total cancellation fees: {total}.")
    return True

def most_popular_room(bookings):
    if not bookings:
        print("\nThere are no bookings in the system.")
        return False
    
    print(f"\n--------- MOST POPULAR ROOM ---------")
    rooms = {}

    for booking in bookings:
        if booking["status"] == "Active":
            if booking["room_id"] not in rooms:
                rooms[booking["room_id"]] = 1
            else:
                rooms[booking["room_id"]] += 1

    most_popular_room = max(rooms, key=rooms.get)
    print(f"\nMost popular room: {most_popular_room} ({rooms[most_popular_room]} bookings).")
    return True

def bookings_per_room(bookings):
    if not bookings:
        print("\nThere are no bookings in the system.")
        return False
    
    print(f"\n--------- BOOKINGS PER ROOM ---------")
    rooms = {}

    for booking in bookings:
        if booking["status"] == "Active":
            if booking["room_id"] not in rooms:
                rooms[booking["room_id"]] = 1
            else:
                rooms[booking["room_id"]] += 1
    
    for room, bookings in rooms.items():
        print(f"\nRoom: {room}, Bookings: {bookings}")
    
    return True

def room_occupancy_rate(bookings):
    rooms = load_rooms_data()
    room_id = get_room_id(rooms)
    date = get_booking_date(past=True)

    for room in rooms:
        if room["room_id"] == room_id:
            duration = room["duration"]

    games = 0
    for booking in bookings:
        if booking["room_id"] == room_id and booking["booking_date"] == date:
            games += 1

    games = games * (duration + RESERVED_TIME)
    full_day = 60 * 12 # 720
    occupancy_rate = (100 / full_day) * games

    print(f"\nOccupancy rate: {occupancy_rate:.2f}% (room ID: {room_id}, date: {date}).")
    return True


def reports_managment():
    back_to_main_menu = False
    while not back_to_main_menu:
        bookings = load_bookings_data()
        print("""
========= REPORTS MANAGEMENT =========

1. All Active Bookings
2. All Cancelled Bookings
3. Total Revenue From Active Bookings
4. Total Cancellation Fees From Cancelled Bookings
5. The Most Popular Room By Number Of Active Bookings
6. Number Of Bookings Per Room
7. The Occupancy Rate Of A Specific Room On A Given Date
8. Back To Main Menu
        """)

        choice = get_choice(8)    

        if choice == 1:
            total_active_bookings(bookings)
        elif choice == 2:
            total_cancelled_bookings(bookings)
        elif choice == 3:
            total_revenue(bookings)
        elif choice == 4:
            total_cancellation_fees(bookings)
        elif choice == 5:
            most_popular_room(bookings)
        elif choice == 6:
            bookings_per_room(bookings)
        elif choice == 7:
            room_occupancy_rate(bookings)
        elif choice == 8:
            back_to_main_menu = True