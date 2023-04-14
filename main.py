import os
import time
import config
import psutil
import requests
import socket


def get_external_ip():
    url = 'https://api.ipify.org?format=json'
    response = requests.get(url)
    data = response.json()
    return data['ip']


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{config.TG_TOKEN}/sendMessage"
    payload = {
        "chat_id": config.CHAT_ID,
        "text": f"{config.SERVER_NAME}\n"
                f"{socket.gethostname()}\n"
                f"({get_external_ip()})\n\n"
                f"{message}",
    }
    requests.post(url, json=payload)


while True:
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage = (load5 / os.cpu_count()) * 100
    if cpu_usage > config.CPU_USAGE:
        send_telegram_message(f'CPU usage is above {round(cpu_usage)}% for last 5 minutes')
    ram_usage = psutil.virtual_memory()[3] / psutil.virtual_memory().total * 100
    if ram_usage > config.RAM_USAGE:
        send_telegram_message(f'RAM usage is above {round(ram_usage)}%')
    hdd = psutil.disk_usage('/')
    disk_space_percent_free = round(hdd.free / hdd.total * 100)
    if disk_space_percent_free < config.DISK_FREE_SPACE:
        send_telegram_message(f'Free disk space is {disk_space_percent_free}% now')
    time.sleep(15)
