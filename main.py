from helpers import *
from rooms import *
from bookings import *
from reports import *

def main():
    exiting = False

    while not exiting:
        print("""
=================================
           ESCAPE ZONE
       Escape Room System
=================================

1. Rooms Management
2. Sales Management
3. Reports
4. Exit
        """)

        choice = get_choice(4)

        if choice == 1:
            rooms_managment()
        elif choice == 2:
            bookings_managment()
        elif choice == 3:
            reports_managment()
        elif choice == 4:
            print("\nExiting...")
            exiting = True
    
    return 0

if __name__ == "__main__":
    main()