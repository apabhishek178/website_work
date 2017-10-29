temp=int(input("enter the temperature in kelvin"))
def convert(temp):
    if(temp<0):
        raise Exception(temp)
    temp1 = ((temp - 273) * 1.8) / 30
    return temp
try:
    f=convert(temp)
    print(f)
except Exception as e:
    print("error in temperature, cannot be colder than 0K")

finally:
    print("program ends")