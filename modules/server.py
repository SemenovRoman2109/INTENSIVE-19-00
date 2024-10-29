import socket

server_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) 
server_socket.bind(("178.136.159.28", 8080))