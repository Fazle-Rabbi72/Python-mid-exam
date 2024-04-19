def view_available_seats(self, id):
        
        print("Available Seats:")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] == '0':
                    print(f"Seat: ({row},{col})")