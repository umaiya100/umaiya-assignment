def get_hypotenuse(adjacent: float|int, opposite: float|int, ):
   hypotenuse = ((adjacent**2)+(opposite**2))**.5
   return hypotenuse

adjacent = float(input("enter the length of one side:"))
opposite = float(input("enter the length of the other side:"))

hypotenuse =((adjacent**2)+(opposite**2))**.5
print(f"the length of hypotenuse is {hypotenuse}")