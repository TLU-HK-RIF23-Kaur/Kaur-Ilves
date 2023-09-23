import praktikum1.task1

def start_practicum1_task(task_number):
    function_name = f"task_{task_number}"
    if callable(globals().get(function_name)):
        func = globals()[function_name]
        result = func()
        return result
    else:
        return f"Task_{task_number} does not exist"

start_practicum1_task(int(input("Sisesta ülesande number: ")))
