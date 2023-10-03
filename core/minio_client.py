import grpc
import minio_service_pb2_grpc
import minio_service_pb2

def upload_file(stub, bucket_name, object_name, file_path):
    request = minio_service_pb2.FileUploadRequest(
        bucket_name=bucket_name,
        object_name=object_name,
        file_path=file_path
    )
    response = stub.UploadFiles(request)
    if response.success:
        print('File uploaded successfully.')
    else:
        print('File upload failed:', response.message)

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = minio_service_pb2_grpc.MinioServiceStub(channel)

    bucket_name = 'kursach4-backend-test1'
    object_name = 'Object.txt'
    file_path = 'C:\\Object.txt'  # Corrected the file path

    upload_file(stub, bucket_name, object_name, file_path)

if __name__ == '__main__':
    main()