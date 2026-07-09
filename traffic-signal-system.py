while True:
    color = input("Enter the color: ").capitalize()
    match color[0]:
        case 'R':
            print("STOP! , SIGNAL IS RED")
        case 'Y':
            print("GET READY >...")
        case 'G':
            print("YOU CAN GO >>>")