import psutil
import time
import datetime
import os
import socket

monitoring_interval = 5
memory_threshold = 80

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
log_filename = f"{current_date}-pub.log"


def log_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    num_logical_cpus = psutil.cpu_count(logical=True)
    used_memory = psutil.virtual_memory().percent
    used_disk_space = psutil.disk_usage('/').percent
    current_host_ip = get_host_ip()

    log_line = f"{datetime.datetime.now()}, {cpu_usage}, {num_logical_cpus}, {used_memory}%, {used_disk_space}%, {current_host_ip}\n"

    with open(log_filename, 'a') as log_file:
        log_file.write(log_line)


def check_memory_threshold():
    used_memory = psutil.virtual_memory().percent
    if used_memory > memory_threshold:
        notification_filename = f"{current_date}-notification.log"
        with open(notification_filename, 'w') as notification_file:
            notification_file.write(
                "Low memory: System is running low on available memory.")


def get_host_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except Exception as e:
        return "N/A"


if __name__ == "__main__":
    if not os.path.exists(log_filename):
        with open(log_filename, 'w') as log_file:
            log_file.write(
                "Timestamp, CPU Usage (%), Logical CPUs, Memory Usage (%), Disk Space Usage (%), Host IP\n")

    while True:
        log_system_info()
        check_memory_threshold()
        time.sleep(monitoring_interval)
