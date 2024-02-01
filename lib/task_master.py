def task_master(text):
    formatted = str(text).lower()
    #if formatted[0:5] == "#todo":
    if "#todo" in formatted:
        return f"Your outstanding task is: {text}."
    
    return "No outstanding tasks to do."