

human_years = int(input("enter the human years:"))

dog_years =0

for i in range(human_years):

 if human_years <= 2:
        dog_years = human_years*10.4
print(dog_years)

if human_years > 2:

 dog_years = human_years*4

print(f" {human_years +1} years of a human is equal to {dog_years} dog years")