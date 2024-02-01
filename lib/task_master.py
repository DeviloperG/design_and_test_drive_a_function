def task_master(text):
    formatted = str(text).lower()
    
    if "#todo" in formatted:
        return f"Your outstanding task is: {text}."
    elif "todo" in formatted:
        return f"This might be an outstanding task: {text}."
    
    return "No outstanding tasks to do."
