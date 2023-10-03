import grpc
import time
from minio.error import S3Error
import logging  # Добавлен импорт модуля logging
import minio_service_pb2
import minio_service_pb2_grpc
from minio import Minio
from concurrent import futures

# Устанавливаем конфигурацию логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MinioServicer(minio_service_pb2_grpc.MinioServiceServicer):
    def __init__(self, minio_client):
        self.minio_client = minio_client

    def UploadFile(self, request, context):
        try:
            with open(request.file_path, 'rb') as f:
                file_content = f.read()
            self.minio_client.put_object(
                bucket_name=request.bucket_name,
                object_name=request.object_name,
                data=file_content,
                length=len(file_content)
            )
            return minio_service_pb2.UploadFileResponse(success=True)
        except S3Error as err:
            return minio_service_pb2.UploadFileResponse(success=False, error_message=str(err))


def serve():
    minio_client = Minio('localhost:9000', access_key='a6MBx3BtEuKu9PllCOtK',
                         secret_key='r1pdDjSfCp6lpAGxCqIdVU72PeVZH2hbOYkUEFti', secure=False)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    minio_service_pb2_grpc.add_MinioServiceServicer_to_server(
        MinioServicer(minio_client), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started and is listening on port 50051')
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
        print('Server stopped')


if __name__ == '__main__':
    serve()
