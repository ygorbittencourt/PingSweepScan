# -*- coding: utf-8 -*-
"""
FOR USE WITH PYTHON 2.7 
Ping Sweep Scan 
Versao 1
By Ygor Bittencourt
https://www.linkedin.com/in/ygorbittencourt/
"""
import sys
import subprocess
import socket

def is_host_up(target_host):
    try:
        subprocess.check_output(["ping", "-c", "1", target_host], stderr=subprocess.STDOUT, universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False

def scan_ports(target_host, ports):
    for port in ports:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(1)  # Define o tempo limite de conexão em segundos
        result = client_socket.connect_ex((target_host, port))
        if result == 0:
            print("A porta {} está aberta em {}".format(port, target_host))
        client_socket.close()

def main():
    if len(sys.argv) < 3:
        print("Uso: python nome_do_programa.py endereco_inicial endereco_final")
        sys.exit(1)


    try:
        start_ip = sys.argv[1]
        end_ip = sys.argv[2]
        
    except socket.error:
        print("Formato de endereços inválido. Certifique-se de fornecer endereços IPv4 válidos.")
        sys.exit(1)

    ports_to_scan = [22, 21, 3389, 80, 443, 8000, 8080, 3306, 1433]  # Portas


    for ip_int in range(int(socket.inet_aton(start_ip).encode("hex"), 16),
                        int(socket.inet_aton(end_ip).encode("hex"), 16) + 1):
        target_host = socket.inet_ntoa(hex(ip_int)[2:].zfill(8).decode("hex"))
        if is_host_up(target_host):
            print("{} está UP".format(target_host))
            scan_ports(target_host, ports_to_scan)

if __name__ == "__main__":
    main()
