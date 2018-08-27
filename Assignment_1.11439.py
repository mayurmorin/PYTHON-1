
# coding: utf-8

# Task 1.1: Install Jupyter Notebook and run the first program and share the output of the program.
# 
# Answer: Below is attached screen shot for your reference

# ![Assignment%20Task%201.1.PNG](attachment:Assignment%20Task%201.1.PNG)

# Task 1.2: Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.

# In[1]:


newlst=[]
for int_i in range(2000, 3201):
    if (int_i%7==0) and (int_i%5!=0):
        newlst.append(str(int_i))
print(','.join(newlst))


# Task 1.3: Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

# In[2]:


firstname = input('Please enter your First Name : ')
lastname = input('Please enter your Last Name : ')
print(lastname[::-1] + ' ' + firstname[::-1])


# Task 1.4:Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r3

# In[3]:


# pi value has taken as 3.141592653
pi = 3.141592653
#radius is half of diameter
r = 12/2 
V = (4/3)*pi*(r**3)
print('Volume of a sphere with diameter 12 cm is :', V)


# Task 2.1: Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.

# In[4]:


commasepnum=input('Kindly enter a sequence of comma-separated numbers : ')
print("List : ",commasepnum.split(","))


# Task 2.2: Create the below pattern using nested for loop in Python.

# In[5]:


for star in range(0,5,1):
    print('*' * star)
for star in range(5,0,-1):
    print('*' * star)


# Task 2.3: Write a Python program to reverse a word after accepting the input from the user.

# In[6]:


inputstr = input('Kindly enter a word to reverse : ')
print('Entered reversed word is : ', inputstr[::-1])


# Task 2.4: Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens

# In[7]:


formatstring="WE, THE PEOPLE OF INDIA,{0:5} having solemnly resolved to constitute India into a SOVEREIGN,{1:5} SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC {2:5} and to secure to all its citizens"
print(formatstring.format('\n','!\n\t','\n\t'))

