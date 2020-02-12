'''
Циклы '''
# while
print("Numbers < 10 (while):")
i=0
while (i<10):
    print(i, end=" ") # print in one line
    i += 1
print("\n")
# i = 10
# for
print("Numbers < 10 (for): ")
for i in range(0,10):
    print(i, end=" ")
else:
    print("\nThe next number is 10\n" )
# i = 9
# break
sum = 0
for i in range(0,100):
    print (i,sum ,end =" ")
    if i > 10:
        print("\nWe reached the end, final sum: ", sum)
        break
sum += i
#sum =11, i=11
# continue i=0
while i<=15:
    if i % 3 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1
print("\n")
# pass
print("Let's print numbers again!")
for i in range(0,10):
    pass
    print(i, end=" ")
print("\n\n")

# от 0 до 500 включительно
for i in range (501):
    if i%7 == 0:
        print (i, end=", ")
else:
    print ("\nAll numbers were printed")

print ("\n")
i=0

while (i<=500):
    print (i, end=", ")
    i+=7
else:
    print ("\nAll numbers were printed")

