import tools
import os
from cryptography.fernet import Fernet, MultiFernet
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers.aead import AESCCM

def Algo1(data, key):
	f = Fernet(key)
	#target_file = open("raw_data/store_in_me.enc","wb")
	#secret_data = f.encrypt(data)
	#target_file.write(secret_data)
	#target_file.close()
	with open("raw_data/store_in_me.enc", "wb") as target_file: 
		secret_data = f.encrypt(data) 
		target_file.write(secret_data)

def Algo1_extented(filename, key1, key2):
	f = MultiFernet([Fernet(key1),Fernet(key2)])
	source_filename = 'files/' + filename
	target_filename = 'encrypted/' + filename
	with open(source_filename, 'rb') as file: 
		raw = file.read() # Read the entire file as bytes 
	secret_data = f.encrypt(raw) 
	with open(target_filename, 'wb') as target_file:
		target_file.write(secret_data)

   # with open(source_filename, 'rb') as file: 
	    #raw = file.read() # Read the entire file as bytes 
    #secret_data = f.encrypt(raw) 
    #with open(tarename, 'wb') as target_file:
	 # target_file.write(secret_d
def Algo2(filename, key, nonce):
	aad = b"authenticated but unencrypted data" # Ensure aad is bytes 
	chacha = ChaCha20Poly1305(key) 
	source_filename = 'files/' + filename # Ensure this variable is correctly defined 
	target_filename = 'encrypted/' + filename
	#a= 'files/' + filename
	#target_filename = 'encrypted/' + filename
	#file = operce_filename,'rb')
	#target_file = open(target_filename,'wb')
	#raw =
	#for line in file:
	#	raw = raw +line
	#secret_data = chacha.encrypt(nonce, raw, aad)
	#target_file.write(secret_data)
	#file.close()
	#target_file.close()
	with open(source_filename, 'rb') as file: 
		raw = file.read() # Read the entire file as bytes 
	secret_data = chacha.encrypt(nonce, raw, aad) 
	with open(target_filename, 'wb') as target_file: 
			target_file.write(secret_data)


def Algo3(filename, key, nonce):
	aad = b"authenticated but unencrypted data"
	aesgcm = AESGCM(key)
	source_filename = 'files/' + filename
	target_filename = 'encrypted/' + filename
	#file = open(source_filename,'rb')
	#target_file = open(target_filename,'wb')
	#raw = b""
	#for line in file:
#		raw = raw + line#
	#secret_data = aesgcm.encrypt(nonce, raw, aad)
	#target_file.write(secret_data)
	#file.close()
	#target_file.close()
	with open(source_filename, 'rb') as file: 
		raw = file.read() # Read the entire file as bytes 
	secret_data = aesgcm.encrypt(nonce, raw, aad) 
	with open(target_filename, 'wb') as target_file:
		target_file.write(secret_data)
	
def Algo4(filename, key, nonce):
	aad = b"authenticated but unencrypted data"
	aesccm = AESCCM(key)
	source_filename = 'files/' + filename
	target_filename = 'encrypted/' + filename
	#file = open(source_filename,'rb')
	#target_file = open(target_filename,'wb')
	#raw = b""
	#for line in file:
#		raw = raw + line#
	#secret_data = aesccm.encrypt(nonce, raw, aad)
	#target_file.write(secret_data)
	#file.close()
	#target_file.close()
	with open(source_filename, 'rb') as file: 
		raw = file.read() # Read the entire file as bytes 
	secret_data = aesccm.encrypt(nonce, raw, aad) 
	with open(target_filename, 'wb') as target_file:
		target_file.write(secret_data)


def encrypter():
	tools.empty_folder('key')
	tools.empty_folder('encrypted')
	key_1 = Fernet.generate_key()
	key_1_1 = Fernet.generate_key()
	key_1_2 = Fernet.generate_key()
	key_2 = ChaCha20Poly1305.generate_key()
	key_3 = AESGCM.generate_key(bit_length=128)
	key_4 = AESCCM.generate_key(bit_length=128)
	nonce13 = os.urandom(13)
	nonce12 = os.urandom(12)
	files = sorted(tools.list_dir('files'))
	for index in range(0,len(files)):
		if index%4 == 0:
			Algo1_extented(files[index],key_1_1,key_1_2)
		elif index%4 == 1:
			Algo2(files[index],key_2,nonce12)
		elif index%4 == 2:
			Algo3(files[index],key_3,nonce12)
		else:
			Algo4(files[index],key_4,nonce13)
	delimiter = b":::::"
	#secret_information = (key_1_1)+":::::"+(key_1_2)+":::::"+(key_2)+":::::"+(key_3)+":::::"+(key_4)+":::::"+(nonce12)+":::::"+(nonce13)
	secret_information = delimiter.join([key_1_1, key_1_2, key_2, key_3, key_4, nonce12, nonce13])
	Algo1(secret_information,key_1)
	#public_key = open("./key/Taale_Ki_Chabhi.pem","wb")
	#public_key.write(key_1)
	#public_key.close()
	#tools.empty_folder('files')
	with open("./key/Taale_Ki_Chabhi.pem", "wb") as public_key: 
		public_key.write(key_1) 
	tools.empty_folder('files')
