from art import tprint

# from src.modules.task_2 import *
# from src.modules.task_3 import *
# from src.modules.task_4 import *
# from src.modules.task_5 import *
# from src.modules.task_6 import *
from src.modules.task_7 import *

# Для проверки результата вызывайте функцию из файла модуля

if __name__ == "__main__":
    tprint("Skillbox")
    try:
        f7_4()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
