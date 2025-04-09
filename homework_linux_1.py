import subprocess
import datetime

result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
output = result.stdout.split("\n")
cpu_total = 0
mem_total = 0

processes_list = []
users_dict = {}

for string in output[1:-1]:
    row = string.split()

    user = row[0]
    process_pid = row[1]
    process_name = row[10][:20]
    cpu = float(row[2])
    mem = float(row[3])

    if user not in users_dict:
        users_dict[user] = {process_pid: [process_name, cpu, mem]}
    else:
        users_dict[user][process_pid] = [process_name, cpu, mem]

    processes_list.append(
        {
            "pid": process_pid,
            "process_name": process_name,
            "user": user,
            "cpu": cpu,
            "mem": mem,
        }
    )

    cpu_total = cpu_total + cpu
    mem_total = mem_total + mem

max_memory_process = max(processes_list, key=lambda process: process["mem"])
max_cpu_process = max(processes_list, key=lambda process: process["cpu"])

print("Отчёт о состоянии системы:")

print("Пользователи системы:", ", ".join(users_dict.keys()))

print(f"Процессов запущено: {len(processes_list)}")
print()
print("Пользовательских процессов:")
for key, value in users_dict.items():
    print(f"{key} {len(value)}")
print()
print(f"Всего памяти используется: {round(mem_total, 1)}%")
print(f"Всего CPU используется: {round(cpu_total, 1)}%")

print(f"Больше всего памяти использует: ({max_memory_process['process_name']})")
print(f"Больше всего CPU использует:  ({max_cpu_process['process_name']})")

filename = datetime.datetime.now().strftime('%d-%m-%Y-%H:%M-scan.txt')
with open(filename, 'w') as f:
    f.write('Отчёт о состоянии системы:\n')
    f.write('Пользователи системы: {}\n'.format(', '.join(users_dict.keys())))
    f.write('Процессов запущено: {}\n'.format(len(processes_list)))
    f.write('')
    f.write('Пользовательских процессов:\n')
    for key, value in users_dict.items():
        f.write('{}: {}\n'.format(key, len(value)))
    f.write('')
    f.write('Всего памяти используется: {} \n'.format(round(mem_total, 1)))
    f.write('Всего CPU используется: {} \n'.format(round(cpu_total, 1)))
    f.write('Больше всего памяти использует: ({})\n'.format(max_memory_process['process_name']))
    f.write('Больше всего CPU использует: ({})\n'.format(max_cpu_process['process_name']))
