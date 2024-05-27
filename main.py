'''
Program to calculate sum of odd number from 1 to 50
'''

sum_of_odd = 0

for i in range(1,50,2):
    sum_of_odd += i
print("The sum of odd number from 1 to 50 is: ", sum_of_odd)    

#2
sum_of_odd = sum(range(1,50,2))
print("The sum of odd number from 1 to 50 is: ", sum_of_odd)
