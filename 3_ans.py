def entry_show(self, id, movie_name, time):

    self.show_list.append((id, movie_name, time))
    self.seats[id] = [['0' for i in range(self.cols)] for j in range(self.rows)]  