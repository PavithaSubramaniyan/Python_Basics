#int to float/str/bool/complex

print("DataType Conversion from integer")
a = int(input("Enter a number: "))
intToFloat = float(a)
intToBoolean = bool(a)
intToString= str(a)
intToComplex = complex(a)
print(intToFloat, intToBoolean , intToString, intToComplex)

#float to int/str/bool/complex
print()
print("DataType Conversion from float")
floatVal = float(input("Enter a float value: "))
print(int(floatVal), str(floatVal), bool(floatVal), complex(floatVal))

#String to int/float/bool/complex
print()
print("DataType conversion from String Value")
strVal =input("Enter a string: ")   #here i no need to add str because
print(int(strVal), float(strVal), bool(strVal), complex(strVal))

#Complex to int/float/str/bool
print()
print("DataType Conversion from complex value")
complexVal = complex(input("Enter a complex value: "))

#Type error while converting int to complex value
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#it doesn't allow to convert complex into int or float , so need to separate real and imaginary value

realVal = complexVal.real
print("From Complex to", type(realVal).__name__+"Conversion is ",int(realVal),"\n",
      "From Complex to",type(realVal).__name__+"Conversion is",float(realVal),"\n",
      "From Complex to",type(complexVal).__name__,"Conversion is",bool(complexVal), "\n",
    "From Complex to",type(complexVal).__name__,"Conversion is",complex(complexVal),"\n")

print(f"From Complex to {type(realVal).__name__} Conversion is {int(realVal)}\n From Complex to {type(float(realVal)).__name__} Conversion is {float(realVal)}\n"
       )

print("From Complex to {} Conversion is {} \n".format(type(complexVal).__name__,int(realVal)))
