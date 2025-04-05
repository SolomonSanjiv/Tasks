#client code
import socket
import pickle
class RPCClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def call(self, obj_name, method_name, *args, **kwargs):
        request = (obj_name, method_name, args, kwargs)
        data = pickle.dumps(request)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(data)
            response = s.recv(4096)
        return pickle.loads(response)
if __name__ == '__main__':
    client = RPCClient('localhost', 8000)
    result = client.call('Calculator', 'add', 5, 10)
    print(f"Result of addition: {result}")