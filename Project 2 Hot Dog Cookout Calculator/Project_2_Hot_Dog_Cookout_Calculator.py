#Project 2 - Hot Dog Cookout Calculator
#Calculates: 
# the number of packages of hot dogs 
# the number of packages of hot dog buns needed
# minimum amount of leftovers for hot dogs and buns

#Prompt user for the number of people attending the cookout
#Prompt user of how many hot dogs will each person get
#Hot dog package = 10
#Hot dog buns package = 8

#Output should display the following:
# The minimum number of packages of hot dogs required
# The minimum number of packages of hot dog buns required
# The number of hot dogs that will be left over
# The number of hot dog buns that will be left over

hot_dogs = 10
hot_buns = 8

people = int(input("How many people will be attending the cookout: "))
give_dog = int(input("How many hot dogs will each person be given: "))

total_doggers = people * give_dog

#div mod as an alternative to avoid having to use // or %
def hotdogowners (apple,orange):
    apple = divmod(apple, orange)
    return apple

def ketchup (fruit, mango):
    fruit = fruit - mango
    return fruit

#taking two arguments
hotdog_package, dog_leftover = hotdogowners(total_doggers, hot_dogs)
buns_needed, bun_leftover = hotdogowners(total_doggers, hot_buns)

if dog_leftover != 0:
    hotdog_package += 1
    dog_leftover = ketchup(hot_dogs,dog_leftover)

if bun_leftover != 0:
    buns_needed += 1
    bun_leftover = ketchup(hot_buns,bun_leftover)


print("\n")
print("Minimum number of packages of hot dogs required: ", hotdog_package)
print("Minimum number of packages of hot dog buns required: ", buns_needed)
print("The number of hot dogs that will be left over: ", dog_leftover)
print("The number of hot dog buns that will be left over: ", bun_leftover)
print("\n")
