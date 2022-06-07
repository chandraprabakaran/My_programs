import psutil
import os
print(psutil.cpu_percent())
print(psutil.cpu_stats())
print(psutil.cpu_times())
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_stats())
print(psutil.cpu_freq())
for x in range(3):
    print(psutil.cpu_times_percent(interval=1, percpu=False))
for x in range(3):
    print(psutil.cpu_percent(interval=1))
for x in range(3):
    print(psutil.cpu_percent(interval=1, percpu=True))
# memory
print("Memory",psutil.virtual_memory())
print("swap",psutil.swap_memory())
l1, l2, l3 = psutil.getloadavg()
CPU_use = (l3/os.cpu_count()) * 100

print(CPU_use)

for proc in range(3):
    print(psutil.Process().open_files())