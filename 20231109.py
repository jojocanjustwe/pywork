# creating a function using def keyword
def pythonista_function():
    print("Welcome to the Python world")
    
#calling the function    
pythonista_function()

def addNumbers(x,y):
    sum = x + y
    return sum

output = addNumbers(12,9)
print(output)

def myFruits(f1,f2,f3,f4):
    FruitsList = [f1,f2,f3,f4]
    return FruitsList
    
output = myFruits("Apple","Bannana","Grapes","Orange")
print(output)

def myAnimals(a1,a2,a3):
    Animalgroup = {'Kitten':a1,'Puppy':a2,'Pup':a3}
    return Animalgroup

output = myAnimals("Cat","Dog","Rat")
print(output)

def  myVeggies(v1,v2,v3):
    vegtuple = (v1,v2,v3)
    return vegtuple

output = myVeggies("Carrot","Potato","Tomato")
print(output)

def myChocolates(cList):
    for i in cList:
        print(i)

chocolateList = ["Dairy Milk","Snickers","Kitkat"]
myChocolates(chocolateList)

def myVehicles(vDict):
        print(vDict)

vehicleDictionary = {
    'Tesla': 'Car',
    'Royal Enfield' : 'Bike'
    }
    
myVehicles(vehicleDictionary)

def Car(name,model):
    print(name)
    print(model)
    
Car("Audi","Q7")

def Car(name,model):
    print(name)
    print(model)
    
Car(model="Q7",name="Audi")