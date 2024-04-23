class Hall:
    def __init__(self, rows, cols, hall_no):
        
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}  
        self.show_list = [] 

        Star_Cinema.entry_hall(self)
