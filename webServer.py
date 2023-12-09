import socket
import os

def tcp_server():
    SERVER_HOST = "localhost"
    SERVER_PORT = 8080

    sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock_server.bind((SERVER_HOST, SERVER_PORT))

    sock_server.listen()

    print("Server ready....")

    while True:
        sock_client, client_address = sock_server.accept()

        request = sock_client.recv(1024).decode()
        print("Dari Client:"+request)

        try:
            response = handle_request(request)
        except FileNotFoundError:
            response = NotFoundError(request)

        sock_client.send(response.encode())
        sock_client.close()
    #endwhile
    sock_server.close()

def handle_request(request):
    # Mendapatkan metode, path, dan protokol dari permintaan HTTP
    method, path, protocol = request.split("\r\n")[0].split()

    # Jika path adalah "/" (root), ubah menjadi "/hyperlink.html"
    if path == "/":
        path = "/hyperlink.html"

    # Mendapatkan jalur file yang diminta
    file_path = os.path.join("html", path[1:])

    # Membaca isi file yang diminta
    with open(file_path, 'r') as file:
        message_body = file.read()

    # Membuat baris respons HTTP
    response_line = "HTTP/1.1 200 OK\r\n"

    # Menentukan tipe konten respons sebagai "text/html"
    content_type = "Content-Type: text/html\r\n\r\n"

    # Menggabungkan baris respons, tipe konten, dan isi pesan
    response = response_line + content_type + message_body

    return response

def NotFoundError(request):
    # Mendapatkan metode, path, dan protokol dari permintaan HTTP
    method, path, protocol = request.split("\r\n")[0].split()

    # Jika path adalah "/" (root), ubah menjadi "/tidak_ketemu.html"
    if path == "/":
        path = "/tidak_ketemu.html"

    # Mendapatkan jalur file yang diminta
    file_path = os.path.join("html", path[1:])

    # Membaca isi file yang diminta
    with open(file_path, 'r') as file:
        message_body = file.read()

    # Membuat baris respons HTTP
    response_line = "HTTP/1.1 404 Not Found\r\n"

    # Menentukan tipe konten respons sebagai "text/html"
    content_type = "Content-Type: text/html\r\n\r\n"

    # Menggabungkan baris respons, tipe konten, dan isi pesan
    response = response_line + content_type + message_body

    return response

if __name__ == "__main__":
    tcp_server()
