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
        
        if TODO present in text
            return "This might be an outstanding task: {text}."

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests



_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
def test_given_expected_string_format():
"""
Given a string with #TODO included at the beginning.
It returns "Your outstanding task is: {text}."
"""
task_master("#TODO buy eggs") => "Your outstanding task is: #TODO buy eggs"

"""
Given a string without #TODO included
It returns "No outstanding tasks to do."
"""
task_master("Buy eggs") => "No outstanding tasks to do."

"""
Given an empty string.
It returns "No outstanding tasks to do."
"""
task_master(" ") => "No outstanding tasks to do."

"""
Given a non-string argument, stringify the argument
Returns "No outstanding tasks to do."
"""
task_master(12345) => "No outstanding tasks to do."

"""
Given a string with #TODO included at the end.
It returns "Your outstanding task is: {text}."
"""
task_master("buy sausages #TODO") => "Your outstanding task is: buy sausages #TODO"

"""
Given a string with #TODO included within it.
It returns "Your outstanding task is: {text}."
"""
task_master("I need #TODO my homework.") => "Your outstanding task is: I need #TODO my homework."

"""
Given a string with multiple #TODO included within it.
It returns "Your outstanding task is: {text}."
"""
task_master("#TODO I need #TODO my homework.") => "Your outstanding task is: #TODO I need #TODO my homework."

"""
Given a string with TODO (missing #) included at the end.
It returns "Your outstanding task is: {text}."
"""
task_master("buy sausages TODO") => "This might be an outstanding task: buy sausages TODO"

"""
Given a string with #todo (lowercase) included at the end.
It returns "Your outstanding task is: {text}."
"""
task_master("buy eggs #todo") => "Your outstanding task is: buy eggs #todo"

"""
Given a string with #TodO (mixed case) included at the end.
It returns "Your outstanding task is: {text}."
"""
task_master("buy eggs #TodO") => "Your outstanding task is: buy eggs #TodO"



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