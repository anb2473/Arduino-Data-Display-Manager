import threading
import socket

import serial
import hashlib
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class Server:
    def __init__(self):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.hostname = socket.gethostname()
        self.ipaddress = '71.191.185.5'  # socket.gethostbyname(self.hostname)

        if not os.path.exists('server.txt'):
            self.password = hashlib.sha256(input('Please enter a password: ').encode('utf-8')).hexdigest()
            self.com_port = input('Please enter a COM port: ')
            self.baud = input('Please enter a baudrate: ')
            self.port = int(input('Please enter a port: '))
            with open('server.txt', 'w') as f:
                f.write(f'{self.password}\n{self.baud}\n{self.com_port}\n{self.port}')
        else:
            update_data: str = input('Start data found, do you wish to override? (y/n)\n')
            if update_data.lower().startswith('y'):
                self.password = hashlib.sha256(input('Please enter a password: ').encode('utf-8')).hexdigest()
                self.com_port = input('Please enter a COM port: ')
                self.baud = input('Please enter a baudrate: ')
                self.port = int(input('Please enter a port: '))
                with open('server.txt', 'w') as f:
                    f.write(f'{self.password}\n{self.baud}\n{self.com_port}\n{self.port}')
            else:
                with open('server.txt', 'r') as f:
                    self.password = f.readline().strip()
                    self.baud = f.readline().strip()
                    self.com_port = f.readline().strip()
                    self.port = int(f.readline().strip())
        os.system('cls' if os.name == 'nt' else 'clear')
        self.arduino = serial.Serial(port=self.com_port, baudrate=int(self.baud), timeout=.1)

        self.server_socket.bind((self.ipaddress, self.port))
        self.server_socket.listen(1)

        print("Setup Finished")
        print("server listening on " + self.ipaddress)

    def run(self):
        while True:
            print()
            client_socket, addr = self.server_socket.accept()
            connection = ServerConnection(client_socket, self.password, self.arduino)
            connection.start()
            print("Connection from " + str(addr))
            print()


def decrypt(aesgcm, message, nonce):
    return aesgcm.decrypt(nonce, message, None)


def encrypt(aesgcm, message, nonce):
    return aesgcm.encrypt(nonce, message, None)


class ServerConnection(threading.Thread):
    def __init__(self, client_socket, password, arduino):
        super().__init__()

        self.symmetric_key = AESGCM.generate_key(bit_length=256)

        self.socket = client_socket
        self.arduino = arduino
        self.password = password

        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

        self.client_public_key_pem = self.socket.recv(2048)
        self.client_public_key = serialization.load_pem_public_key(self.client_public_key_pem)

        # Encrypt the symmetric key with the client's public key
        self.encrypted_symmetric_key = self.client_public_key.encrypt(
            self.symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        self.socket.send(self.encrypted_symmetric_key)

        aesgcm = AESGCM(self.symmetric_key)
        in_data = self.socket.recv(1024)
        nonce = self.socket.recv(12)
        in_data = decrypt(aesgcm, in_data, nonce)
        self.failed = False

        if hashlib.sha256(in_data).hexdigest() == self.password:
            self.socket.send(encrypt(aesgcm, self.key, nonce))
            print("Authentication successful")
        else:
            self.failed = True

    def write_read(self):
        data = self.arduino.readline()
        return data

    def run(self):
        if self.failed:
            raise Exception('Authentication error')
        while True:
            try:
                value = self.write_read()
                self.socket.send(self.cipher_suite.encrypt(value))
            except:
                raise Exception("User closed connection")


if __name__ == "__main__":
    app = Server()
    app.run()
