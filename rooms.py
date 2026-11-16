from helpers import *
from json_handler import *

def display_rooms(rooms):
    if not rooms:
        print("\nNo rooms exists.")
        return

    print("\n--------- DETAILES OF ALL ROOMS ---------")
    for room in rooms:
        print_room(room)
    return

def display_room_details(rooms):
    if not rooms:
        print("\nNo rooms exists.")
        return

    room_id = get_room_id(rooms)
    print(F"\n--------- DETAILES OF ROOM {room_id} ---------")
    for room in rooms:
        if room["room_id"] == room_id:
            print_room(room)
            return

def add_room(rooms):
    print(F"\n--------- ADD ROOM ---------")
    
    room = {
        "room_id": create_unique_room_id(rooms),
        "name": get_name(),
        "difficulty": get_room_difficulty(),
        "duration": get_room_duration(),
        "min_players": None,
        "max_players": None,
        "price_per_player": get_price_per_player(),
        "is_active": get_active_status()
    }
    room["min_players"] = get_min_players()
    room["max_players"] = get_max_players(room["min_players"])

    rooms = load_rooms_data()
    rooms.append(room)
    save_rooms_data(room)
    return

def update_room_details(rooms):
    print(F"\n--------- UPDATE ROOM ---------")
    room_id = get_room_id(rooms)

    print("\nWhich detail do you want to update?")
    print("""
1. Name
2. Difficulty
3. Duration
4. Minimum Players
5. Maximum Players
6. Price Per Player
    """)

    choice = get_choice(7)

    for room in rooms:
        if room["room_id"] == room_id:
            if choice == 1:
                room["name"] = get_name()
            elif choic == 2:
                room["difficulty"] = get_room_difficulty()
            elif choice == 3:
                room["duration"] = get_room_duration()
            elif choice == 4:
                room["min_players"] = get_min_players()
            elif choice == 5:
                room["max_players"] = get_max_players()
            elif chioce == 6:
                room["price_per_player"] = get_price_per_player()
            print(f"\nRoom {room_id} updated successfully.")

            save_rooms_data(rooms)
            return

def room_active_status(rooms):
    print(F"\n--------- ROOM ACTIVE STATUS ---------")
    print("\nFor which room would you like to change the active status?")
    room_id = get_room_id(rooms)
    active_status = get_active_status()

    for room in rooms:
        if room["room_id"] == room_id:
            room["is_active"] = active_status

            save_rooms_data(rooms)
            return


def rooms_managment():
    back_to_main_menu = False
    while not back_to_main_menu:
        rooms = load_rooms_data()
        print("""
========= PRODUCTS MANAGEMENT =========

1. Display All Rooms
2. Display Room Details
3. Add Room
4. Update Room
5. Room Active Status
6. Back to Main Menu
        """)

        choice = get_choice(6)
    
        if choice == 1:
            display_rooms(rooms)
        elif choice == 2:
            display_room_details(rooms)
        elif choice == 3:
            add_room(rooms)
        elif choice == 4:
            update_room_details(rooms)
        elif choice == 5:
            room_active_status(rooms)
        elif choice == 6:
            back_to_main_menu = True
    
    return