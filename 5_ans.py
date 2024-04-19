def view_show_list(self):
        print("Show List:")
        for show in self.show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")