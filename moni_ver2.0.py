import os
import psutil
import sys

# import colorama
# colorama.init()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def get_name():
    return{
        "Имя системы": os.name,
        "Имя пользователя": os.getlogin()
    }
def get_cpu_load():
    return psutil.cpu_percent(interval=1, percpu=True)

def get_progress_bar(percentage, length=100):
    filled_length = int(length * percentage // 100)
    bar = "|" * filled_length + "-" * (length - filled_length)
    return bar

def print_cpu_status(cpu_loads):
    print("Загрузка ядер CPU:")
    for i, load in enumerate(cpu_loads):
        bar = get_progress_bar(load)
        cpu_label = f"Ядро {i+1}:".rjust(8)
        print(f"{cpu_label} [{bar}] {load:5.1f}%".ljust(106))

def move_cursor_up(lines):
    sys.stdout.write(f"\033[{lines}A")

def main():
    cpu_count = psutil.cpu_count(logical=True)
    clear_console()
    print("Загрузка ядер CPU:")
    for _ in range(cpu_count):
        print(f"Ядро _: [{'-' * 100}]   0.0%")
    try:
        while True:
            cpu_loads = get_cpu_load()
            move_cursor_up(cpu_count + 1)  
            print_cpu_status(cpu_loads)
    except KeyboardInterrupt:
        clear_console()

if __name__ == '__main__':
    n=get_name()
    for key, value in n.items():
        print(key, value)
    main()