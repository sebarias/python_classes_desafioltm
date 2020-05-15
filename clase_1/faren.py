""" faren = int(input("ingrese los farenheit: "))
celsius = (faren - 32) // 1.8
print("los {} farenheit son {} celsius".format(faren,int(celsius))) """

#solucion con sys y funcion
import sys

def to_celsius(grades):
    return int((grades -32) // 1.8)

def to_farenheit(grades):
    return int(grades * 1.8 + 32)

grades = int(sys.argv[1])
grades_type = sys.argv[2]
if grades_type == "celsius":
    print(to_celsius(grades))
else:
    print(to_farenheit(grades))

number = 10
while number > 0:
    print(number)
    number -=1 


