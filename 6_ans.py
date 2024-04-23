def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print("Invalid show ID.")
            return

        print(f"Available seats for Show ID {show_id}:")
        for i in range(self.rows):
            for j in range(self.cols):
                if self.seats[show_id][i][j]:
                    print("|O|", end=" ")
                else:
                    print("(B)", end=" ")
            print()
