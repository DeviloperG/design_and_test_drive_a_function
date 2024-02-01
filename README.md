# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem
Design and test-drive a function 📡🌶️🌶️

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.

"""
Function will take a string, look up "#TODO" and: 
if present return the string with a message.
if #TODO not present then return "No tasks to do."
"""

## 2. Design the Function Signature


_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def task_master(text):
    """

    Parameters: (list all parameters and their types)
        text: string (e.g. '#TODO complete program.')

    Returns: (state the return value and its type)
        if #TODO present in text
            return "Your outstanding task is: {text}."

        if #TODO not present in text
            return "No outstanding tasks to do."

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string with #TODO included
It returns the return "Your outstanding task is: {text}."
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```