def day_type():

    day = input().strip().capitalize()

    if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        print("Working day")
    elif day in ["Saturday", "Sunday"]:
        print("Weekend")
    else:
        print("Error")

day_type()
