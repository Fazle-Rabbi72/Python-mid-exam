class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.show_list = []
        self.seats = {} 

        Star_Cinema().entry_hall(self) 