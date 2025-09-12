day=int(input("enter the number"))
month=int(input("enter the number"))
match day:
    case 1|2|3|4|5|6|7 if month==4:
        print("weekdays of april")
    case 1|2|3|4|5|6|7 if month==5:
        print("weekdays of may")   
    case _:
        print("no match ")