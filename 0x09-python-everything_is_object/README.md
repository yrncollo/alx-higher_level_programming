# 0x09.Python - Everything is object

## Resources

- [9.10.Objects and values](https://alx-intranet.hbtn.io/rltoken/MrtBogRzYETxnSKG97E7Sg)
- [9.11.Aliasing](https://alx-intranet.hbtn.io/rltoken/Ro-7kVXtmWyAeOXEw7RhSg)
- [Immutable vs mutable types](https://alx-intranet.hbtn.io/rltoken/X1lEmkwQRWI3fP4W7bq_qw)
- [Mutation](https://alx-intranet.hbtn.io/rltoken/HpKOdgDg6GIoBoG0UPOgPA)(only this chapter)
- [9.12.Cloning lists](https://alx-intranet.hbtn.io/rltoken/-Gi4PX4srBYFKpZ5Er6sqA)
- [Python tuples:immutable but potentially changing](https://alx-intranet.hbtn.io/rltoken/NZIom4L-tS0HjpY_uEVr9A)

## Objectives

- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

## Tasks

0.What function would you use to print the type of an object?

    Write the name of the function in the file, without ()

**Solution [0-answer.txt](0-answer.txt)**

1.How do you get the variable identifier (which is the memory address in the CPython implementation)?

    Write the name of the function in the file, without ().

**Solution [1-answer.txt](1-answer.txt)**

2.In the following code, do a and b point to the same object? Answer with Yes or No.
**Solution [2-answer.txt](2-answer.txt)**

```
>>> a = 89
>>> b = 100
```

3.In the following code, do a and b point to the same object? Answer with Yes or No.
**Solution [3-answer.txt](3-answer.txt)**

```
>>> a = 89
>>> b = 89
```

4.In the following code, do a and b point to the same object? Answer with Yes or No.
**Solution [4-answer.txt](4-answer.txt)**

```
>>> a = 89
>>> b = a
```

5.In the following code, do a and b point to the same object? Answer with Yes or No.
**Solution [5-answer.txt](5-answer.txt)**

```
>>> a = 89
>>> b = a + 1
```

6.What do these 3 lines print?
**Solution [6-answer.txt](6-answer.txt)**

```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

7.What do these 3 lines print?
**Solution [7-answer.txt](7-answer.txt)**

```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

8.What do these 3 lines print?
**Solution [8-answer.txt](8-answer.txt)**

```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

9.What do these 3 lines print?
**Solution [9-answer.txt](9-answer.txt)**

```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

10.What do these 3 lines print?
**Solution [10-answer.txt](10-answer.txt)**

```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```

11.What do these 3 lines print?
**Solution [11-answer.txt](11-answer.txt)**

```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
```

12.What do these 3 lines print?
**Solution [12-answer.txt](12-answer.txt)**

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

13.What do these 3 lines print?
**Solution [13-answer.txt](13-answer.txt)**

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

14.What do these 3 lines print?
**Solution [14-answer.txt](14-answer.txt)**

```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

15.What does this script print?
**Solution [15-answer.txt](15-answer.txt)**

```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

16.What does this script print?
**Solution [16-answer.txt](16-answer.txt)**

```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

17.What does this script print?
**Solution [17-answer.txt](17-answer.txt)**

```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

18.What does this script print?
**Solution [18-answer.txt](18-answer.txt)**

```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

19.Write a function `def copy_list(l):` that returns a **copy** of a list.

- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module

**Solution [19-copy_list.py](19-copy_list.py)**

```
guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py
3 19-copy_list.py
guillaume@ubuntu:~/0x09$
```

20. `a = ()`
    Is a a tuple? Answer with Yes or No.
    **Solution [20-answer.txt](20-answer.txt)**

21. `a = (1, 2)`
    Is a a tuple? Answer with Yes or No.
    **Solution [21-answer.txt](21-answer.txt)**

22. `a = (1)`
    Is a a tuple? Answer with Yes or No.
    **Solution [22-answer.txt](22-answer.txt)**

23. `a = (1,)`
    Is a a tuple? Answer with Yes or No.
    **Solution [23-answer.txt](23-answer.txt)**

24.What does this script print?
**Solution [24-answer.txt](24-answer.txt)**

```
a = (1)
b = (1)
a is b
```

25.What does this script print?
**Solution [25-answer.txt](25-answer.txt)**

```
a = (1, 2)
b = (1, 2)
a is b
```

26.What does this script print?
**Solution [26-answer.txt](26-answer.txt)**

```
a = ()
b = ()
a is b
```

27.

```
>>> id(a)
>>> 139926795932424
>>> a
>>> [1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

Will the last line of this script print 139926795932424? Answer with Yes or No.
**Solution [27-answer.txt](27-answer.txt)**

28.

```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

Will the last line of this script print 139926795932424? Answer with Yes or No.
**Solution [28-answer.txt](28-answer.txt)**

29.Write a function `magic_string()` that returns a string “BestSchool” n times the number of the iteration (see code):

- Format: see example
- Your file should be maximum 4-line long (no documentation needed)
- You are not allowed to import any module

**Solution [100-magic_string.py](100-magic_string.py)**

````

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py
4 100-magic_string.py
guillaume@ubuntu:~/0x09$

```

30.Write a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.

- You are not allowed to import any module

**Solution [101-locked_class.py](101-locked_class.py)**

```

guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$

````

31.

```
julien@ubuntu:/python3$ cat int.py
a = 1
b = 1
julien@ubuntu:/python3$
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

- How many int objects are created by the execution of the first line of the script? (103-line1.txt)
  **Solution [103-line1.txt](103-line1.txt)**
- How many int objects are created by the execution of the second line of the script (103-line2.txt)
  **Solution [103-line2.txt](103-line2.txt)**

32.

```
    julien@ubuntu:/python3$ cat int.py
    a = 1024
    b = 1024
    del a
    del b
    c = 1024
    julien@ubuntu:/python3$
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

- How many int objects are created by the execution of the first line of the script? (`104-line1.txt`)
  **Solution [104-line1.txt](104-line1.txt)**
- How many int objects are created by the execution of the second line of the script (`104-line2.txt`)
  **Solution [104-line2.txt](104-line2.txt)**
- After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (`104-line3.txt`)
  **Solution [104-line3.txt](104-line3.txt)**
- After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (`104-line4.txt`)
  **Solution [104-line4.txt](104-line4.txt)**
- How many int objects are created by the execution of the last line of the script (104-line5.txt)
  **Solution [104-line5.txt](104-line5.txt)**

33.

```
julien@twix:/tmp/so$ cat int.py
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

- Before the execution of line 2 (`print("Love")`), how many int objects have been created and are still in memory? (`105-line1.txt`)
  **Solution [105-line1.txt](105-line1.txt)**
- Why? (optional blog post :))
  Hint: `NSMALLPOSINTS`, `NSMALLNEGINTS`

34.

```
  guillaume@ubuntu:/python3$ cat string.py
  a = "SCHL"
  b = "SCHL"
  del a
  del b
  c = "SCHL"
  guillaume@ubuntu:/python3$
```

Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

- How many string objects are created by the execution of the first line of the script? (`106-line1.txt`)
  **Solution [106-line1.txt](106-line1.txt)**
- How many string objects are created by the execution of the second line of the script (`106-line2.txt`)
  **Solution [106-line2.txt](106-line2.txt)**
- After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (`106-line3.txt`)
  **Solution [106-line3.txt](106-line3.txt)**
- After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (`106-line4.txt`)
  **Solution [106-line4.txt](106-line4.txt)**
- How many string objects are created by the execution of the last line of the script (`106-line5.txt`)
  **Solution [106-line5.txt](106-line5.txt)**

```

```
