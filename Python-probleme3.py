select_option = int(input("choose an option"))
match select_option:
    case 1:
        print("Veiw Marks")
    case 2:
        print("Veiw Attendence")
    case 3:
        print("Veiw Time Table")
    case 4:
        print("View Fee Details")
    case _:
        print("Invalid")
