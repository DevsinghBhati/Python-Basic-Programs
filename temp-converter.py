def feren_to_cel():
    feren = float(input("Enter the temprature in farenheat: "))
    celcius = lambda feren : (feren - 32) * 5/9
    print(f"{celcius(feren)} Celcius")

def cel_to_feren():
    celcius = float(input("Enter the temprature in farenheat: "))
    feren =  lambda celcius : ( celcius *9/5 ) + 32
    print(f"{feren(celcius)} Ferhenheit" )


print("|| TEMPRATURE CONVERTER ||")
print("1. FERHENHEIT TO CELCIUS\n2. CELCIUS TO FERHENHEIT")
choice = int(input("Enter operation : "))
if(choice == 1):
    feren_to_cel()
    
if(choice == 2):
    cel_to_feren()