a = input("Enter the letters as per the requirment\n1:OPPOSITE\n2:ADJACENT\n3:DIAGONAL\n")
b = a.split(",")
print(b)
s = int(input("Enter the value"))
d = int(input("Enter the value"))
if "1" and "2" in b :
    print(f"The value diagonal is {s*s+d*d}")
elif '1' or '2' and '3' in b :
    print(f"The value is {d*d-s*s}")