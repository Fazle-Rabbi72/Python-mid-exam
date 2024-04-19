class Star_Cinema:
    _hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._show_list = []
        self._seats = {} 

        Star_Cinema().entry_hall(self)  

        
    def entry_show(self, id, movie_name, time):

        self._show_list.append((id, movie_name, time))
        self._seats[id] = [['0' for i in range(self._cols)] for j in range(self._rows)] 

    def book_seats(self, id, seat_list):
        if id not in [show[0] for show in self._show_list]:
            print("Invalid ID")
            return
        for seat in seat_list:
            row, col = seat
            if self._seats[id][row][col] != '0':
                print(f"Seat ({row},{col}) is already booked!")
            else:
                self._seats[id][row][col] = 'Booked'
        print("Seats booked successfully!")

    def view_show_list(self):
        print("Show List:")
        for show in self._show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid ID")
            return
        print("Available Seats:")
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[id][row][col] == '0':
                    print(f"Seat: ({row},{col})")


hall = Hall(10, 10, 1)

hall.entry_show(111, "Spider Man1", '19-4-2024 12.00 PM')
hall.entry_show(112, "Avengers", '20-4-2024 12.00 PM')


while True:
    print("\nOptions:")
    print("1. View all shows")
    print("2. View available seats")
    print("3. Book tickets")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        hall.view_show_list()
    elif choice == '2':
        show_id = input("Enter the show ID: ")
        hall.view_available_seats(show_id)
    elif choice == '3':
        show_id = input("Enter the show ID: ")
        num_seats = int(input("Enter the number of seats to book: "))
        seat_list = []
        for i in range(num_seats):
            seat = tuple(map(int, input(f"Enter seat {i+1} (row,col): ").split(',')))
            seat_list.append(seat)
        hall.book_seats(show_id, seat_list)
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Please enter a valid option.")

