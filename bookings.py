from helpers import *
from datetime import *
from json_handler import *
from constants import *


def calculate_discount(price, players):
    if players <= 4:
        print("\nNot eligible for discount.")
        return price
    if players <= 6:
        print("\nEligible for 10% discount!")
        return price - (price * 0.10)
    print("\nEligible for 15% discount!")
    return price - (price * 0.15)

def weekend_price(total, booking_date):
    booking_date = datetime.strptime(booking_date, "%Y-%m-%d")
    if booking_date.weekday() > 4:
        print("\nWeekend price, 15% added.")
        return total + (total * 0.15)
    print("\nNot weekend, original price.")
    return total

def calculate_total(rooms, room_id, players, booking_date):
    for room in rooms:
        if room["room_id"] == room_id:
            total = calculate_discount(room["price_per_player"] * players, players)
            total = weekend_price(total, booking_date)
            return round(total, 2)

def create_booking(bookings):
    print(F"\n--------- CREATE BOOKING ---------")
    rooms = load_rooms_data()
    
    customer_name = get_name()
    room_id = room_is_active(rooms)
    booking_date = get_booking_date()
    start_time = get_start_time()
    if not can_book_room(rooms, room_id, booking_date, start_time, bookings):
        return
    players = get_players(rooms, room_id)
    total_price = calculate_total(rooms, room_id, players, booking_date)

    booking = {
        "booking_id": create_unique_booking_id(bookings),
        "customer_name": customer_name,
        "room_id": room_id,
        "booking_date": booking_date,
        "start_time": start_time,
        "players": players,
        "total_price": total_price,
        "status": "Active",
        "cancellation_fee": 0.0
    }

    bookings.append(booking)
    save_bookings_data(bookings)
    return

def display_bookings(bookings):
    if not bookings:
        print("\nThere are no bookings in the system.")
        return

    print(F"\n--------- DISPLAY BOOKINGS ---------")
    counter = 0
    for booking in bookings:
        print_booking(booking)
        counter += 1
    print(f"\n{counter} bookings.")
    return

def search_booking_by_id(bookings):
    if not bookings:
        print("\nThere are no bookings in the system.")
        return

    print(F"\n--------- SEARCH BOOKING BY ID ---------")
    booking_id = get_booking_id(bookings)
    for booking in bookings:
        if booking["booking_id"] == booking_id:
            print_booking(booking)
            return

def display_customer_booking(bookings):
    if not bookings:
        print("\nThere are no bookings in the system.")
        return

    print(F"\n--------- DISPLAY CUSTOMER'S BOOKING ---------")
    customer_name = get_name()
    counter = 0
    for booking in bookings:
        if booking["customer_name"] == customer_name:
            print_booking(booking)
            counter += 1
    
    if counter > 0:
        print(f"\n{counter} bookings for {customer_name}.")
        return
    print(f"\nNo bookings found for {customer_name}.")
    return

def display_bookings_by_date(bookings):
    if not bookings:
        print("\nThere are no bookings in the system.")
        return

    print(F"\n--------- DISPLAY BOOKINGS BY DATE ---------")
    booking_date = get_booking_date()
    counter = 0
    for booking in bookings:
        if booking["booking_date"] == booking_date:
            print_booking(booking)
            counter += 1
    
    if counter > 0:
        print(f"{counter} bookings found for {booking_date}.")
        return
    print(f"No bookings found for {booking_date}.")
    return

def update_date(bookings, booking_id, room_id, players):
    booking_date = get_booking_date()
    start_time = get_start_time_by_id(bookings, booking_id)
    rooms = load_rooms_data()
    if not can_book_room(rooms, room_id, booking_date, start_time, bookings, update=True, booking_id=booking_id):
        return
    
    for booking in bookings:
        if booking["booking_id"] == booking_id:
            total_price = calculate_total(rooms, room_id, players, booking_date)
            booking["booking_date"] = booking_date
            booking["total_price"] = total_price
            save_bookings_data(bookings)
            print(f"\nBooking {booking_id} date updated successfully - {booking_date} (total: {total_price}).")
            return

def update_time(bookings, booking_id, room_id, players):
    booking_date = get_booking_date_by_id(bookings, booking_id)
    start_time = get_start_time()
    rooms = load_rooms_data()
    if not can_book_room(rooms, room_id, booking_date, start_time, bookings, update=True, booking_id=booking_id):
        return
    
    for booking in bookings:
        if booking["booking_id"] == booking_id:
            total_price = calculate_total(rooms, room_id, players, booking_date)
            booking["start_time"] = start_time
            booking["total_price"] = total_price
            save_bookings_data(bookings)
            print(f"\nBooking {booking_id} start time updated successfully - {start_time} (total: {total_price}).")
            return

def update_players(bookings, booking_id, room_id, players):
    booking_date = get_booking_date_by_id(bookings, booking_id)
    rooms = load_rooms_data()
    players = get_players(rooms, room_id)

    for booking in bookings:
        if booking["booking_id"] == booking_id:
            total_price = calculate_total(rooms, room_id, players, booking_date)
            booking["players"] = players
            booking["total_price"] = total_price
            save_bookings_data(bookings)
            print(f"\nBooking {booking_id} players updated successfully - {players} (total: {total_price}).")
            return

def update_booking(bookings):
    if not bookings:
        print("\nThere are no bookings in the system.")
        return

    print(f"\n--------- UPDATE BOOKING ---------")
    print(f"\nWhich booking would you like to update?")
    booking_id = get_booking_id(bookings)
    result, room_id, players = room_not_active(bookings, booking_id, load_rooms_data())
    if result:
        print(f"\nRoom for this booking {room_id} is not active.")
        return
    
    print("""
1. Update Date
2. Update Start Time
3. Update Number Of Players""")

    choice = get_choice(3)

    if choice == 1:
        update_date(bookings, booking_id, room_id, players)
    elif choice == 2:
        update_time(bookings, booking_id, room_id, players)
    elif choice == 3:
        update_players(bookings, booking_id, room_id, players)
    
    return

def update_cancelled_booking(bookings, booking_id, fee=True, hours=None):
    for booking in bookings:
        if booking["booking_id"] == booking_id:
            if booking["status"] == "Cancelled":
                print(f"\nBooking {booking_id} is already cancelled.")
                return False

            if not fee:
                print(f"\nMore than 24 hours, no cancellation fee applied.")
                booking["status"] = "Cancelled"
                booking["cancellation_fee"] = NO_CANCELLATION_FEE
                save_bookings_data(bookings)
                return True
            
            if hours is None:
                raise ValueError("\nThe 'hours' argument is required when fee=True.")

            if hours >= 6:
                cancellation_fee = booking["total_price"] * 0.25
                print(f"\nBetween 6 to 24 hours before game, 25% cancellation fee applied.")
            else:
                cancellation_fee = booking["total_price"] * 0.50
                print(f"\nLess than 6 hours before game, 50% cancellation fee applied.")

            booking["status"] = "Cancelled"
            booking["cancellation_fee"] = cancellation_fee
            save_bookings_data(bookings)
            return True

def cancel_booking(bookings):
    if not bookings:
        print("\nThere are no bookings in the system.")
        return

    print(f"\n--------- CANCLE BOOKING ---------")
    print(f"\nWhich booking would you like to cancel?")
    booking_id = get_booking_id(bookings)

    booking_date = get_booking_date_by_id(bookings, booking_id)
    start_time = get_start_time_by_id(bookings, booking_id)

    combined_str = f"{booking_date} {start_time}"
    booking_date_time = datetime.strptime(combined_str, "%Y-%m-%d %H:%M")
    now = datetime.now()

    difference = booking_date_time - now
    if difference.days > 0:
        update_cancelled_booking(bookings, booking_id, fee=False)
    else:
        hours_left = difference.total_seconds() / 3600
        if hours_left <= 0:
            print(f"\nBooking {booking_id} is already past.")
            return
        update_cancelled_booking(bookings, booking_id, hours=hours_left)
    return

def bookings_managment():
    back_to_main_menu = False
    while not back_to_main_menu:
        bookings = load_bookings_data()
        print("""
========= BOOKINGS MANAGEMENT =========

1. Create New Booking
2. Display All Bookings
3. Search Booking By ID
4. Display Customer's Booking
5. Display Bookings By Date
6. Update Booking
7. Cancel Booking
8. Back to Main Menu
        """)

        choice = get_choice(8)    

        if choice == 1:
            create_booking(bookings)
        elif choice == 2:
            display_bookings(bookings)
        elif choice == 3:
            search_booking_by_id(bookings)
        elif choice == 4:
            display_customer_booking(bookings)
        elif choice == 5:
            display_bookings_by_date(bookings)
        elif choice == 6:
            update_booking(bookings)
        elif choice == 7:
            cancel_booking(bookings)
        elif choice == 8:
            back_to_main_menu = True
    
    return