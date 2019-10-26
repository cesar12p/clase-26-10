def main():
    a=int(input("Ingrese Salario"))
    if(a>1000):
        desc=a*.15
        sueldo=a-desc
        print("Sueldo: "+str(sueldo)+" Se desconto:"+str(desc))
    else:
        desc=a*.12
        sueldo=a-desc
        print("Sueldo: "+str(sueldo)+" Se desconto:"+str(desc))
        
if __name__ == "__main__":
    main()