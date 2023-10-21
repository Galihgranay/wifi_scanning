import pywifi
import time
from tabulate import tabulate

# Fungsi untuk memindai jaringan Wi-Fi yang tersedia
def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0] 
    iface.scan() 
    time.sleep(2)  

    scan_results = iface.scan_results()
    return scan_results

# Fungsi untuk mencetak daftar jaringan Wi-Fi yang ditemukan dalam bentuk tabel
def print_wifi_list(wifi_list):
    unique_networks = {}
    for result in wifi_list:
        ssid = result.ssid
        if ssid not in unique_networks:
            unique_networks[ssid] = [result.signal, result.akm[0] if result.akm else "Open"]

    table = []
    for index, (ssid, data) in enumerate(unique_networks.items(), 1):
        signal_strength, security = data
        table.append([index, ssid, signal_strength, security])

    headers = ["No.", "SSID", "Signal Strength", "Security"]
    print(tabulate(table, headers, tablefmt="pretty"))

if __name__ == "__main__":
    wifi_list = scan_wifi()
    print_wifi_list(wifi_list)
