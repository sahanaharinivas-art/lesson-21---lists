start = int(input("enter start number:"))
end = int(input("enter end number:"))

squares = []
even = []
odd = []

for i in range (start, end + 1):
    sq = i * i 
    squares.append(sq)
    
    if sq % 2 == 0:
        even.append(sq)
    else:
        odd.append(sq)

print("Squares:", squares)
print("Even squares:", even)
print("Odd squares:", odd)