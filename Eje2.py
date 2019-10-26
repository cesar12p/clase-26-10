def main():
    a=int(input("Ingrese su salario"))
    b=int(input("Ingrese su categoria ej: 1 2 3 4"))
    if(b==1):
        desc=a*.15
        sueldo=a+desc
    elif(b==2):
        desc=a*.10
        sueldo=a+desc
    elif(b==3):
        desc=a*.08
        sueldo=a+desc
    elif(b==4):
        desc=a*.07
        sueldo=a+desc
    print("Aumento: "+str(desc)+" Sueldo Total: "+str(sueldo))
if __name__ == "__main__":
    main()