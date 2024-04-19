def view_available_seats(self, id):
        if id not in self.seats:
            print("Invalid ID")
            return
        print("Available Seats:")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] == '0':
                    print(f"Seat: ({row},{col})")

def book_seats(self, id, seat_list):
        if id not in [show[0] for show in self.show_list]:
            print("Invalid ID")
            return
        for seat in seat_list:
            row, col = seat
            if self.seats[id][row][col] != '0':
                print(f"Seat ({row},{col}) is already booked!")
            else:
                self.seats[id][row][col] = 'Booked'
        print("Seats booked successfully!")