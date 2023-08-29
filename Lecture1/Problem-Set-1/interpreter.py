expression = input("Expression: ")

x, y, z = expression.split(" ")

match y:
    case "+":
        answer = float(x) + float(z)
        print('%.1f' % answer)
    case "-":
        answer = float(x) - float(z)
        print('%.1f' % answer)
    case "*":
        answer = float(x) * float(z)
        print('%.1f' % answer)
    case "/":
        answer = float(x) / float(z)
        print('%.1f' % answer)