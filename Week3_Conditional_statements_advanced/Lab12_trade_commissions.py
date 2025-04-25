city = input()
sales = float(input())

if sales < 0:
    print("error")
else:
    commission = 0
    match city:
        case "Sofia":
            if 0 <= sales <= 500:
                commission = 0.05
            elif 500 < sales <= 1000:
                commission = 0.07
            elif 1000 < sales <= 10000:
                commission = 0.08
            elif sales > 10000:
                commission = 0.12
            else:
                print("error")
                exit()
        case "Varna":
            if 0 <= sales <= 500:
                commission = 0.045
            elif 500 < sales <= 1000:
                commission = 0.075
            elif 1000 < sales <= 10000:
                commission = 0.10
            elif sales > 10000:
                commission = 0.13
            else:
                print("error")
                exit()
        case "Plovdiv":
            if 0 <= sales <= 500:
                commission = 0.055
            elif 500 < sales <= 1000:
                commission = 0.08
            elif 1000 < sales <= 10000:
                commission = 0.12
            elif sales > 10000:
                commission = 0.145
            else:
                print("error")
                exit()
        case _:
            print("error")
            exit()

    final_commission = sales * commission
    print(f"{final_commission:.2f}")
