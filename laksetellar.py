antall = int(input("Hvor mange laks vil du ha?"))

def laksefunksjon(x):
    if x == 1:
        print("1 laks")
    elif x > 1:
        print("1 laks")
        for i in range(2,x+1):
            print(i,"lakser")
            
        
laksefunksjon(antall)