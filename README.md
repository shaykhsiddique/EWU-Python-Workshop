# Workshop on Python 

![N|Solid](https://i.imgur.com/O87SYPi.png)

Topics:
- [Overview Language](#overview)
- [Environment Setup](#environment-setup)
    - Setup Python3
    - Virtual Environment for web application
- [Basic Syntex](#basic-syntex)
    - Variables
    - Operators
    - Decision making
    - Loops
- [Lists, Tuples, Dictionaries](#lists-tuples-dictionaries)
- [Functions](#functions).
- Modules.
- Problem Solving.
- OOP in Python.
- Python GUI Programming - Tkinter.
- Building a simple application using Tkinter.


## Overview
Scripting vs Programming: Figure out between interpreter and compiler. 
Python's design philosophy emphasizes code readability with its notable use of significant whitespace (*[Wiki](https://en.wikipedia.org/wiki/Python_(programming_language))*).
- Web development (server-side),
- Software development,
- Machine Learning, Statistics, Data Science.
- System scripting.

## Environment Setup
------------------------------
Installing Python3 on:
- **Windows:** Download and install (*[python.org](https://www.python.org/downloads/)*).
    *Command: Based on Environment Path. Default: `python`*
- **Linux:** 
    ```bash 
        $ sudo apt-get update
        $ sudo apt-get install python3
    ```
    *Command: For different versions of installing - python2: `python`, python3: `python3`.*

    >Checking the Current Version of Python: `python --version` or `python3 --version`

## Basic Syntex
------------------------------
**Type of Variables:**
     ![N|Solid](https://i.imgur.com/LO2H6ST.png)

>Indentation is very sensitive in python. Scopes are defined by **semicolon** and **indentation**.    

**Data Type Casting**
```python
    x = float(10)       #value of x will be 10.0
    y = int(5.5)        #value of y will be 2
    z = str(20)         #value of x will be "20"
```

**Operators:**
- Arithmetic Operators: `+`, `-`, `*`, `/`, `+`, `%`, `**`, `//`.
- Assignment Operators: `+=`, `-=`, `*=` etc.
- Comparison Operators: `>`, `<`, `==`, `!=`,`>=`, `<=`.

**Python Decisions:**

*IF ELSE*
```python
    a = 43
    b = 111
    c = 73
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")
```
*Joinning conditions*
```python
    if a > b and a > c:
        print("a is the leargest number of all.")
```
**Loops:**
*While Loop*
```python
    i = 1
    while i < 6:
        print(i)
        i += 1
```
*For Loop*
```python
for x in range(2, 6):
  print(x)
  
#loops in list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
```

## Lists, Tuples, Dictionaries
--------------------------------

## Functions
--------------------------------
