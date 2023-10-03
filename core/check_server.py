import grpc

channel = grpc.insecure_channel('localhost:50051')
print("Попытка подключения к серверу...")
try:
    grpc.channel_ready_future(channel).result(timeout=10)
    print("Сервер доступен и успешно работает!")
except grpc.FutureTimeoutError:
    print("Не удалось подключиться к серверу. Возможно, он не запущен или недоступен.")
