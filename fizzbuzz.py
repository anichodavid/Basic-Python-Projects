def fizzbuzz_plus(n):
    list = {
        3 : "Fizz",
        5 : "Buzz",
        7 : "Bazz"
    }

    result = []
    for index in range(1, n+1):
        output = ""
        for key, value in list.items():
            if index % key == 0:
                output += value

        result.append(output or str(index))

    return result


print(fizzbuzz_plus(4))