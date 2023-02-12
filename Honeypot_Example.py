import socket
import logging

def start_honeypot(port):

    logging.basicConfig(filename='honeypot.log', level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind(('0.0.0.0', port))
    except socket.error as e:
        logging.error(f"Failed to bind socket: {e}")
        return

    s.listen(1)
    logging.info(f"Honeypot listening on port {port}")

    while True:
        try:
            conn, addr = s.accept()
            logging.info(f"Received connection from {addr[0]}")
        except socket.error as e:
            logging.error(f"Failed to accept incoming connection: {e}")
            continue

        try:
            data = conn.recv(1024)
            logging.info(f"Received data: {data}")
        except socket.error as e:
            logging.error(f"Failed to receive data: {e}")
            continue

        try:
            conn.send(b"This is a honeypot, please do not attempt to exploit it.")
        except socket.error as e:
            logging.error(f"Failed to send response: {e}")
            continue

        try:
            conn.close()
        except socket.error as e:
            logging.error(f"Failed to close connection: {e}")
            continue

start_honeypot(80)