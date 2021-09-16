"""LOOPS"""

# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

# 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։


# 4. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։
#nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'

# 5. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։

#1. miqich erkara stachvel

a = []
for i in range(0, 3):
    a.append([])
    if i == 0:
        for j in range(1, 4):
            a[i].append(j ** 2)

    elif i == 1:
        for j in range(4, 7):
            a[i].append(j ** 2)
    elif i == 2:
       for j in range(7, 10):
            a[i].append(j ** 2)

print(a)


#4.

nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'
a = nonsense.lower()
sum = 0
for i in a:
    if i == 'b':
        sum = sum + 1

print(sum)





#5.

n = int(input('Enter a number N : '))
a = 1
for i in range (0, n):
    a = a * (i + 1)
print(a)


