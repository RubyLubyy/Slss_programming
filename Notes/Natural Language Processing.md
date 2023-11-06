
# [Output](https://github.com/teacherubial/programming-2023-2024/blob/main/Notes/1%20-%20Natural%20Language%20Processing.md#output)

We can display text and symbols using output

We use the `print()` function to display output

```python
print()
```

# [Comments](https://github.com/teacherubial/programming-2023-2024/blob/main/Notes/1%20-%20Natural%20Language%20Processing.md#comments)

Comments are pieces of text that are _NOT_ interpreted by Python This means that the text is **ignored** We use the # symbol to make comments
## Variables 
Allow us the store information for the time our app is running

```python
favourite food = input("What is your favourite food?")
```
`favourite_food` -> name of the variable
= -> assignment operator
input... value

# [[Strings]]

## Format Strings
We can evaluate inside of string using f-string
To create an f-string, we put and `f` before the opening quote

```python
fave_food = input ("What's your favourite food?")
print (f"Oooo, {fave_food} sounds good.")
```

# [String Methods](https://github.com/teacherubial/programming-2023-2024/blob/1232e7c4fa9e383c1b392b7f8aa12682fba33df1/Notes/Strings.md#string-methods)

[[Methods]] are functions that we can use on [[Objects]].

String methods allow us to modify and work with strings.

Say for example, we want to make all characters of a string lowercase.

```python
mr_ubial_yelling = "PLEASE PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower())  # lowercases the letters
```

## ``.lower()``

The `.lower()` method takes a string and converts all UPPERCASE characters to lowercase.

We can use `.lower()` to help with [[Errors#Semantic Errors|errors]].

## ``.upper()
The ``.upper`` method converts all lowercase characters to uppercase in a string

## ``.strip(str)
The ``.strip (str)`` method removes characters from the beginning and the end of the string

## ``.split``-> List

## [[Design]]


## [[Lists]]
In python, lists are a collection of items
We store value inside of list
The values of the items can be different `Types`
Order matters in a list

## Creating a List
To make a list, we use brackets \[\] to surround our list
We separate the individual items with commas

```python
some_list = ["Jimmy", "Sara", "Frederique"]
```

## Access Elements in the list
We can access the individual things from lists using bracket notation
In the example below, we'll use bracket notation to access "Sara"

```python
some_list[1]    # "Sara"
some_list[0]    # "Jimmy"
some_list[2]    # "Frederique"
some_list[-1]   # "Frederique", count from end
```

Inside the brackets, we give the *index* of the item we want
Python uses **0-index** counting, which means we start counting at 0
## [[Modules]]
**Modules** are pieces of code that we can borrow in Python
This includes things like function

For example, in `random` we used the `.choice()` function to choose something randomly from lists

These piece of code are **not** automatically included, 
so we need to `import` them into our code explicitly

## Import 
The `import` keyword loads the module into our Python file  
**`import` should be at the top of our file, under the header**

## The `time` module

Time allows us to play around with anything related to time  
Specifically, we can use `time` to pause our code

```python
import time

# Pause our code for 1 second
time.sleep(1)
```

# Errors

# [Syntax Errors](https://github.com/teacherubial/programming-2023-2024/blob/1232e7c4fa9e383c1b392b7f8aa12682fba33df1/Notes/Errors.md#syntax-errors)

These type of errors are ones that occur when you run your code and then it **breaks**.

Syntax errors are relatively easy to _spot_ and _fix_.

**Syntax** errors occur when we don't follow the **rules** of the language completely.

# [Semantic Errors](https://github.com/teacherubial/programming-2023-2024/blob/1232e7c4fa9e383c1b392b7f8aa12682fba33df1/Notes/Errors.md#semantic-errors)

Semantic errors occur when our code doesn't **MEAN** what we intend it to **MEAN**.

These errors, in Mr. Ubial's opinion, are FAR MORE challenging to spot and fix.

```python
user_response = input("Do you like to eat food? ")

if user_response == "yes":
	print("You are a human.")
else:
	print("You must be some sort of robot.")
```

The problem with the code above is subtle. What I (Mr. Ubial) mean is that EVERY ANSWER OF YES should go into the YES block.

We can use `.lower()` to fix this error.

```python
user_response = input("Do you like to eat food? ")

if user_response.lower() == "yes":
	print("You are a human.")
else:
	print("You must be some sort of robot.")
```


# Range (number)
`range( )` is a function that gives you a sequence of numbers starting at 0 by a default. By default it also goes up by 1. It stops right before the number that we provide as input. 

```python
range
```


## Type
In Python, data can be grouped in categories called Types. 

| Name                            | Example              |
| ---                                 | ---                        |
| string or str                  | "hello world! "     |
| list                                 |  [ 1, 2, 3, 4, 5 ]     |
| boolean or bool.          | True. False.          |
| integer or int                | 1  -10  1205          |
| float                              | 1.2 -432.21 1.0.    |

An example showing the use of these names : 

``` python
favourite_food = "bibimbap"
my_age = 16
my_age_float = 16.0
```