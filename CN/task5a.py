#server code
import socket
import pickle
class Calculator:
    def add(self, x, y):
        return x + y
class RPCServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(1)
    def start(self):
        print(f"RPC Server started on {self.host}:{self.port}")
        while True:
            conn, addr = self.socket.accept()
            print(f"Connection established with {addr}")
            data = conn.recv(4096)
            request = pickle.loads(data)
            result = self.process_request(request)
            conn.sendall(pickle.dumps(result))
            conn.close()
    def process_request(self, request):
        obj_name, method_name, args, kwargs = request
        cls = globals()[obj_name]
        instance = cls()
        func = getattr(instance, method_name)
        return func(*args, **kwargs)
if __name__ == '__main__':
    server = RPCServer('localhost', 8000)
    server.start()
