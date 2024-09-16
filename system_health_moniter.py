import psutil
import logging
import time

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

CPU_USAGE_THRESHOLD = 80  
MEMORY_USAGE_THRESHOLD = 80  
DISK_USAGE_THRESHOLD = 80  

MONITOR_INTERVAL = 5

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    return disk_usage.percent

def check_running_processes():
    processes_count = len(psutil.pids())
    logging.info(f"Checked number of running processes: {processes_count}")

def monitor_system_health():
    while True:
        logging.info("Starting system health check...")
        
        cpu_usage = check_cpu_usage()
        memory_usage = check_memory_usage()
        disk_usage = check_disk_usage()
        
        logging.info(f"System usage - CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%")
        
        if cpu_usage > CPU_USAGE_THRESHOLD:
            alert_message = f"ALERT: High CPU usage detected: {cpu_usage}%"
            print(alert_message)
            logging.warning(alert_message)

        if memory_usage > MEMORY_USAGE_THRESHOLD:
            alert_message = f"ALERT: High memory usage detected: {memory_usage}%"
            print(alert_message)
            logging.warning(alert_message)

        if disk_usage > DISK_USAGE_THRESHOLD:
            alert_message = f"ALERT: High disk usage detected: {disk_usage}%"
            print(alert_message)
            logging.warning(alert_message)
        
        check_running_processes()

        logging.info("Completed system health check.")
        time.sleep(MONITOR_INTERVAL)

if __name__ == '__main__':
    print("Starting system health monitoring...")
    logging.info("System health monitoring started.")
    try:
        monitor_system_health()
    except KeyboardInterrupt:
        print("System health monitoring stopped.")
        logging.info("System health monitoring stopped.")
