while True:
    print("\nOptions:")
    print("1. View all shows")
    print("2. View available seats ")
    print("3. Book tickets ")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        hall.view_show_list()
    elif choice == "2":
        show_id = int(input("Enter the show ID: "))
        hall.view_available_seats(show_id)
    elif choice == "3":
        show_id = int(input("Enter the show ID: "))
        num_seats = int(input("Enter the number of seats to book: "))
        seat_list = []
        for i in range(num_seats):
            seat = tuple(map(int, input(f"Enter seat {i+1} (row,col): ").split(',')))
            seat_list.append(seat)
        hall.book_seats(show_id, seat_list)
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
