class Star_Cinema:
    _hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {}
        self._show_list = []

        Star_Cinema().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self._show_list.append((id, movie_name, time))
        self._seats[id] = [[True for i in range(self._cols)] for j in range(self._rows)]

    def book_seats(self, show_id, seat_list):
        if show_id not in self._seats:
            print("Invalid show ID.")
            return

        for seat in seat_list:
            row, col = seat
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print("No Existing Seat For booking")
                continue

            if not self._seats[show_id][row][col]:
                print(f"Seat {row},{col} is already booked.")
            else:
                self._seats[show_id][row][col] = False
                print(f"Seat {row},{col} booked successfully.")

    def view_show_list(self):
        print("Show List:")
        for show_info in self._show_list:
            print(f"ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print("Invalid show ID.")
            return

        print(f"Available seats for Show ID {show_id}:")
        for i in range(self._rows):
            for j in range(self._cols):
                if self._seats[show_id][i][j]:
                    print("|O|", end=" ")
                else:
                    print("(B)", end=" ")
            print()


hall = Hall(10, 10, 1)
hall.entry_show(111, "Avengers", "12:00 PM")
hall.entry_show(112, "Spider Man", "03:00 PM")
while True:
    print("\nOptions:")
    print("1. View all shows")
    print("2. View available seats ")
    print("3. Book tickets ")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        hall.view_show_list()
    elif choice == "2":
        show_id = int(input("Enter the show ID: "))
        hall.view_available_seats(show_id)
    elif choice == "3":
        show_id = int(input("Enter the show ID: "))
        num_seats = int(input("Enter the number of seats to book: "))
        seat_list = []
        for i in range(num_seats):
            seat = tuple(map(int, input(f"Enter seat {i+1} (row,col): ").split(',')))
            seat_list.append(seat)
        hall.book_seats(show_id, seat_list)
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
