def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)


def status_check(status):
    if status >= 12:
        return "Pass"
    else:
        return "Fail"
