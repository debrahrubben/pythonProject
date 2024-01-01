try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print('you cant divide by zero')
except ValueError as e:
    print(e)
    print('divide by number')
except Exception as e:
    print(e)
    print('something went wrong')
else:
    print(result)
finally:print('this will always execute')