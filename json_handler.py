import json
from pathlib import Path

DB_ROOMS_FILE = Path(__file__).parent / "rooms.json"
DB_BOOKINGS_FILE = Path(__file__).parent / "bookings.json"

def load_rooms_data():
    if not DB_ROOMS_FILE.exists():
        print("\nNo database file yet - starting empty")
        return []
    try:
        with open(DB_ROOMS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("\nDatabase file is corrupted - starting empty")
        return []

def save_rooms_data(rooms):
    with open(DB_ROOMS_FILE, "w", encoding="utf-8") as file:
        json.dump(rooms, file, indent=2, ensure_ascii=False)
    print("\nRoom saved successfully!")

def load_bookings_data():
    if not DB_BOOKINGS_FILE.exists():
        print("\nNo database file yet - starting empty (rooms.json).")
        return []
    try:
        with open(DB_BOOKINGS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("\nDatabase file is corrupted - starting empty (bookings.json).")
        return []

def save_bookings_data(bookings):
    with open(DB_BOOKINGS_FILE, "w", encoding="utf-8") as file:
        json.dump(bookings, file, indent=2, ensure_ascii=False)
    print("\nBooking saved successfully!")