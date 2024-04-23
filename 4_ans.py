def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print("Invalid show ID.")
            return

        for seat in seat_list:
            row, col = seat
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                print("No Existing Seat For booking")
                continue

            if not self.seats[show_id][row][col]:
                print(f"Seat {row},{col} is already booked.")
            else:
                self.seats[show_id][row][col] = False
                print(f"Seat {row},{col} booked successfully.")
