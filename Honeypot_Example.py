import socket

def start_honeypot(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('0.0.0.0', port))

    s.listen(1)

    print(f"Honeypot listening on port {port}")

    while True:

        conn, addr = s.accept()
        print(f"Received connection from {addr[0]}")

        data = conn.recv(1024)
        print(f"Received data: {data}")

        conn.send(b"This is a honeypot, please do not attempt to exploit it.")

        conn.close()


start_honeypot(80)