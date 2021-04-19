import socket
import sys
def main(argv):
    python webclient.py www.google.com/index.html -p 80
    python webclient arg1 arg2 arg3
arg1 = www.google.com, arg2 = index.html, arg3 = 80
if len(argv) != 3 : 
    print("Arguments size error")
    sys.exit()
_domain = ""
_file = ""
if(len(argv[0].split("/", 1)) == 1):
	_domain = argv[0]
elif len(argv[0].split("/", 1)) > 1:
    _domain = argv[0].split("/", 1)[0]
    _file = argv[0].split("/", 1)[1]

# this is a standart form of request when we send request to the server
request_msg = "GET /" + _file + " HTTP/1.1\r\nHost: " + _domain + "\r\n\r\n"

# since we can't send string through the web we have to encode it
# into binary bytes
_domain = "www.google.com"
port_num = 80
request = str.encode(request_msg)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#through input we get domain and port number
server_address = (_domain, port_num)
print('connecting to the port', server_address)
#we need to connect when server waits for the connection
#we have unique address of domain(ip address) and port number
client_socket.connect(server_address)
#we are sending the request to the server
client_socket.sendall(request)
# it is when we get response from the server
response = client_socket.recv(10054)
#since response comes in the byte it would be better if we decode it
response.decode()
# if we received an response we would decode it, and print it out
if (len(response)>0):
    while (len(response)>0):
        print(response)
        response = client_socket.recv(10054)
    client_socket.close()

#if the case URL wasn't found on the server
else:
    print("404 That is an error \n The requested URL : "  + argv[0] +  " was not found on this server.")
    client_socket.close()
if __name__ == "__main__":
    main(sys.argv[1:])
