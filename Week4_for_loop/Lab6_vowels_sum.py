input_text = input()

sum = 0
for symbol in input_text:
    match symbol:
        case "a":
            sum += 1
        case "e":
            sum += 2
        case "i":
            sum += 3
        case "o":
            sum += 4
        case "u":
            sum += 5

print(sum)
