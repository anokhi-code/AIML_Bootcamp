#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Q1. Create a list of 5 of your favorite fruits and:
#- Print the list.
#- Add a new fruit to the list.
 # Remove the 2nd item from the list.
#- Print the length of the list.


#- Sort the list alphabetically.

my_list=['apple','orange','cherry','kiwi','banana']
print(my_list)


# In[7]:


last=my_list.pop(1)
my_list


# In[8]:


len(my_list)


# In[9]:


my_list.sort()
my_list


# In[11]:


#Q2. Create a tuple of 4 of your favorite movies.
#- Print the tuple.
#- Try changing one element (observe the error and explain why).
#- Access the last movie using negative indexing.

my_tuple=('conjuring','f1','puspa','kgf')
print(my_tuple)


# In[14]:


my_tuple['f1']='kgf2' #immutability the reason it can be changed becuase in tuple once a value is created it can be changed or modified.


# In[15]:


my_tuple[-1]


# In[ ]:


#Section 3: Sets
    #Q3. Create a set of 5 unique colors.
#- Add a new color to the set.
#- Try adding a duplicate color (observe what happens).
#- Remove a color from the set.
#- Check if a specific color (e.g., "Blue") is in the set.


# In[16]:


my_set={'purple','white','green','ornage','red'}
my_set


# In[18]:


my_set.add('pink')
my_set


# In[20]:


my_set.add('red')
my_set# trying adding existing color but it doesnt show any error it allows to run but doesnt show the error their was on effect of add function in on the set


# In[21]:


if 'blue' in my_set:
    print('Yes it is their')
else:
    print('no')


# In[58]:


#Section 4: Dictionaries
#Q4. Create a dictionary with student names as keys and their marks as values. Example:
#student_marks = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
#- Print all keys and values.
#- Add a new student to the dictionary.
#- Update marks of an existing student.
#- Delete one student from the dictionary.
#- Check if 'David' is a student in the dictionary.

student_marks= {'Alice': 85, 
                'Bob': 92, 
                'Charlie': 78}
print(student_marks)


x = student_marks.keys()
print(x)

x=dict.values()
print(x)


# In[59]:


student_marks.update({'Ryan':86})
print(student_marks)

student_marks.update({'Alice':76})
print(student_marks)


# In[60]:


student_marks.pop('Alice')
print(student_marks)


# In[61]:


if 'David' in student_marks:
    Print('Yes their is a student')
    
else:
    print("Their is no one with name david")


# In[67]:


#Section 5: Conditional Statements
#Q5. Write a Python program that:
#- Accepts a number from the user.
#- Checks if the number is positive, negative, or zero.
#- Prints whether the number is even or odd.

Number=float(input("Enter the number: "))

if Number>0:
    print("It is positive")
    
elif Number<0:
        print("It is negative")
        
else:
    print("It is zero")
    
if Number %2==0:
    print('it is even number')
    
else:
    print('it is odd number')


# In[68]:


#Q6. Write a program to check if a student has passed or failed:
#- Input marks from the user.
#- If marks >= 40, print "Pass", else print "Fail".


Marks=float(input('Enter the marks for the student:'))

if Marks>=40:
    print("Student is pass")
else:
    print("student is fall")
    


# In[78]:


#Q7. Create a simple grading system:
#- Take marks as input.
#- Use the following grading logic:
#Marks Range | Grade
#------------|-------
#90 - 100 | A
#75 - 89 | B
#50 - 74 | C
#40 - 49 | D
#Below 40 | F
#Bonus Challenge:


Mark= float(input("Enter the marks:"))

if Mark>=90:
    print('Student is getting A ')
    
elif Mark>=75:
    print('Student is getting B ')
    
elif Mark>=50:
    print('Student is getting C')

elif Mark>=40:
    print('Student is getting D')

else:
        print('Student is getting F')


# In[91]:


#Q8. Write a program to:
#- Store product names and prices in a dictionary.
#- Ask user to input a product name.
#- Display its price if it exists.
#- If not, display "Product not found".

Inventory= {'Pen': 10, 
            'Book': 20, 
            'Map': 25}
#print(Inventory)

Product=input("Enter product name:")

if Product in Inventory:
    print("Price of",Product, "is", Inventory[Product])
else:
    print('product didnot found')


# In[93]:


#Q9. Use a for loop to print all elements of a list containing your 5 favorite animal.

list_animal=['Dog','Horse','Cow','cat','lion']


for list_animal in list_animal:
    print(list_animal)


# In[98]:


#Q10. Write a program using a for loop to print numbers from 1 to 10.
for i in range(1,11):
    print(i)
    


# In[103]:


#Q11. Write a program using a while loop to print the numbers from 5 to 1 in reverse.

Number= 5

while Number>0:
    print('Reverse number:',Number)
    Number-=1


# In[111]:


#Q12. Use a for loop with range() to print even numbers between 1 and 20.

for i in range(2,21,2):
    print(i)


# In[114]:


#Q13. Write a loop that iterates through numbers 1 to 10, but skips the number 5 using 'continue'.

for i in range(1,11):
    if i == 5:
        continue
    print(i)
    


# In[115]:


#Q14. Write a loop that breaks when it reaches the number 7, but prints all other numbers before it.
for i in range(1,11):
    if i == 7:
        break
    print(i)


# In[ ]:


#Write a program that uses 'pass' in a for loop going from 1 to 3. 


# In[ ]:


#Ask the user to enter numbers continuously using a while loop. Stop asking when the user
#enters 0. Then print the sum of all entered numbers (excluding 0).

