import socket
from cryptography.fernet import Fernet

KEY = b'6_W8V_vR9-9X8S5_S-9v8S5_S-9v8S5_S-9v8S5_S-0=' 
cipher = Fernet(KEY)

IP, PORT = "127.0.0.1", 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_DGRAM = UDP
sock.bind((IP, PORT))

print(f"Server Active. Monitoring Remote Nodes securely...")

while True:
    try:
        encrypted_data, addr = sock.recvfrom(1024)
        
        decrypted_message = cipher.decrypt(encrypted_data).decode()
        node_id, cpu, ram = decrypted_message.split(',')
        
        print(f"Report from {node_id} ({addr}): CPU {cpu}%, RAM {ram}%")
        
        if float(cpu) > 80.0:
            print(f"!!! ALERT: {node_id} is overheating!")

    except Exception as e:
        print(f"Security Alert: Blocked an unauthorized or corrupted packet.")

