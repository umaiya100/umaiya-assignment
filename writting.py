
def is_even(number: float|int) ->bool:

 if number %2 == 0:
    return True
 return False
number = int(input("enter the number:"))
if is_even(number):
  print(f"yes the number {number} is even")
else:
  print(f"no the number {number} is odd:")