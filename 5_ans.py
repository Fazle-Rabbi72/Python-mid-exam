def view_show_list(self):
        print("Show List:")
        for show_info in self.show_list:
            print(f"ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")
