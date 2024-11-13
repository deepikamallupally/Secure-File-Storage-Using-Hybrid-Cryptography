
import tools
from cryptography.fernet import Fernet, MultiFernet
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305, AESGCM, AESCCM

def Algo1(key):
    f = Fernet(key)
    with open("raw_data/store_in_me.enc", "rb") as target_file:
        secret_data = b""
        for line in target_file:
            secret_data += line
        data = f.decrypt(secret_data)
    return data

def Algo1_extented(filename, key1, key2):
    f = MultiFernet([Fernet(key1), Fernet(key2)])
    source_filename = 'encrypted/' + filename
    target_filename = 'files/' + filename
    with open(source_filename, 'rb') as file:
        raw = b""
        for line in file:
            raw += line
        secret_data = f.decrypt(raw)
    with open(target_filename, 'wb') as target_file:
        target_file.write(secret_data)

def Algo2(filename, key, nonce):
    aad = b"authenticated but unencrypted data"
    chacha = ChaCha20Poly1305(key)
    source_filename = 'encrypted/' + filename
    target_filename = 'files/' + filename
    with open(source_filename, 'rb') as file:
        raw = b""
        for line in file:
            raw += line
        secret_data = chacha.decrypt(nonce, raw, aad)
    with open(target_filename, 'wb') as target_file:
        target_file.write(secret_data)

def Algo3(filename, key, nonce):
    aad = b"authenticated but unencrypted data"
    aesgcm = AESGCM(key)
    source_filename = 'encrypted/' + filename
    target_filename = 'files/' + filename
    with open(source_filename, 'rb') as file:
        raw = b""
        for line in file:
            raw += line
        secret_data = aesgcm.decrypt(nonce, raw, aad)
    with open(target_filename, 'wb') as target_file:
        target_file.write(secret_data)

def Algo4(filename, key, nonce):
    aad = b"authenticated but unencrypted data"
    aesccm = AESCCM(key)
    source_filename = 'encrypted/' + filename
    target_filename = 'files/' + filename
    with open(source_filename, 'rb') as file:
        raw = b""
        for line in file:
            raw += line
        secret_data = aesccm.decrypt(nonce, raw, aad)
    with open(target_filename, 'wb') as target_file:
        target_file.write(secret_data)

def decrypter():
    tools.empty_folder('files')
    key_1 = b""
    list_directory = tools.list_dir('key')
    filename = './key/' + list_directory[0]
    with open(filename, "rb") as public_key:
        for line in public_key:
            key_1 += line
    secret_information = Algo1(key_1)
    
    # Split the byte data directly
    delimiter = b":::::"
    list_information = secret_information.split(delimiter)
    
    key_1_1 = list_information[0]
    key_1_2 = list_information[1]
    key_2 = list_information[2]
    key_3 = list_information[3]
    key_4 = list_information[4]
    nonce12 = list_information[5]
    nonce13 = list_information[6]

    files = sorted(tools.list_dir('encrypted'))
    for index in range(len(files)):
        if index % 4 == 0:
            Algo1_extented(files[index], key_1_1, key_1_2)
        elif index % 4 == 1:
            Algo2(files[index], key_2, nonce12)
        elif index % 4 == 2:
            Algo3(files[index], key_3, nonce12)
        else:
            Algo4(files[index], key_4, nonce13)
