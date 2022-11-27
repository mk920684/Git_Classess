## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?
Ans. Python is used for multiple purpose and its not limited for a particular domain. The programming languages which can fulfill the needs of a wide variety of domains are called general purpose programming languages. Use of python can be in Data analysis, machine learning, Web development, Automation or scripting and many more.

Python is very much similar to english language and easily understandable for human hence its called high level language.

Q2. Why is Python called a dynamically typed language?
Ans. Python is called dynamically typed because the type of variables are determined during run time based on the type of value that is getting assigned .

Q3. List some pros and cons of Python programming language?
    Pros:
	1. Easy to understandable
	2. Increase productivity
	3. Dynamically typed, So programmer don't have worried about variable type during declaration.
	4. Vast Collection of Library
	
	Cons:
	1. Little slow as program is not fast when executing codes, since is a dynamically typed and interpreted programming language.
	2. Can throw run time error because of dynamically typed.

Q4. In what all domains can we use Python?
Ans. 1. Data Science
	 2. Data Engineering
	 3. Web Development
	 4. Mobile Application
	 5. AI & Machine Learning
	 6. Automation

Q5. What are variable and how can we declare them?
Ans. Variables are the memory location name where we can store some value and access it by using its name.

		Declaration of variable:
		
		name='Mukesh'
		
		So a variable named 'name' will be created and store string value inside it.

Q6. How can we take an input from the user in Python?
Ans. We can use Input() function for user input.

		Ex: name=Input('Enter Your Name')

Q7. What is the default datatype of the value that has been taken as an input using input() function?
Ans. By default, It return String value irrespective of value provided.

Q8. What is type casting?
Ans. Type Casting is the process of converting value from one type to another type.

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
Ans. Yes, We can take multiple values from user via Input() function but we have to use Split() function at end to seperate input values.
	Ex:
	name, age = input("Enter name and age: ").split()

Q10. What are keywords?
Ans. Keyword are the pre-defined reserved words that is used for special purpose. We can't have any variable name similar to keywords.

Q11. Can we use keywords as a variable? Support your answer with reason.
Ans. No, We can't use keyword as a variable name. Because python will treat that name as reserved word and has special meaning. The compiler has to be able to distinguish between keywords and identifiers (variable names). So thats the reason It throws error.

Q12. What is indentation? What's the use of indentaion in Python?
Ans. indentation means white space at the beginning of code and Python use indentaion to identify block of code.

Q13. How can we throw some output in Python?
Ans. To output something on screen, we use Print() function.
		Ex: Print('Hello')

Q14. What are operators in Python?
Ans. Operators are the special symbols used to perform arithmetical and Logical operation.
	Ex: +, -, //, <, > etc..

Q15. What is difference between / and // operators?
Ans. / --> Refers float division
	// --> Refers Int division

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```

Ans. print('iNeuroniNeuroniNeuroniNeuron')



Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
Ans. 

num1 = int(input('Enter a Number'))
if(num1%2==0):
	print('Even Number')
else:
	print('Odd Number')

Q18. What are boolean operator?
Ans. The logical operator which return true or false are called boolean operator. Ex: or, and, True, False

Q19. What will the output of the following?
Ans.

(True: 1, False: 0 )

1 or 0 -->  True

0 and 0 --> False

True and False and True --> False

1 or 0 or 0 -->True
```

Q20. What are conditional statements in Python?
Ans. We use conditional statements to execute the specific block of code if the given condition is true or false.
     Ex: If(), If() else(), If() elif() else()

Q21. What is use of 'if', 'elif' and 'else' keywords?
Ans. If--> If block will execute only if the given condition is true.
	Ex: if(2==2)
			print('True')
		
		So the above condition is true, following code will execute.
		
	elif--> Its short form of else if. If the previous conditions were not true, then try this condition.
	
	else--> if none of the condition is true, then execute else block.

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
Ans. 

age = int(input('Enter your age'))
if(age>=18):
	print('I can vote')
else:
	print('I Can\'t Vote')

Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
Ans.  

numbers = [12, 75, 150, 180, 145, 525, 50]
size=len(numbers)
num_sum=0
for n in range(size):
	if(numbers[n]%2==0):
		num_sum+=numbers[n]

print('Sum of even number is ',num_sum)


Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
Sol:

num1,num2,num3=input('Enter 3 Numbers').split()
if(num1>num2 and num1>3):
 print(num1)
elif(num2>num3 and num2>num1):
 print(num2)
else:
	print(num3)
	

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```

Sol:

numbers = [12, 75, 150, 180, 145, 525, 50]
size=len(numbers)
for n in range(size):
 if(numbers[n]%5==0):
   if(numbers[n]>150):
    continue
 print(numbers[n])
 if(numbers[n]>500):
  break
	