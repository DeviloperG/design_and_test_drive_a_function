from lib.task_master import *



def test_given_expected_string_format():
    result = task_master("#TODO buy eggs")
    assert result == "Your outstanding task is: #TODO buy eggs."

def test_given_string_missing_hashtag_todo():
    result = task_master("buy eggs")
    assert result == "No outstanding tasks to do."

def test_given_empty_string():
    result = task_master("")
    assert result == "No outstanding tasks to do."

def test_given_non_string():
    result = task_master(12345)
    assert result == "No outstanding tasks to do."

def test_given_hashtag_todo_at_end():
    result = task_master("buy sausages #TODO")
    assert result == "Your outstanding task is: buy sausages #TODO."

def test_given_hashtag_todo_within_string():
    result = task_master("I need #TODO my homework")
    assert result == "Your outstanding task is: I need #TODO my homework."


def test_given_multiple_hashtag_todo():
    result = task_master("#TODO I need #TODO my homework")
    assert result == "Your outstanding task is: #TODO I need #TODO my homework."