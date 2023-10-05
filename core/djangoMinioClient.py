import grpc
from django.views import View
import minio_service_pb2
from .minio_service_pb2_grpc import MinioServiceStub
from django.http import JsonResponse

class MinioDjangoClient(View):
    def post(self, request):
        # Параметры запроса из POST-запроса
        bucket_name = request.POST.get('bucket_name', '')
        object_name = request.POST.get('object_name', '')
        file_content = request.FILES.get('file').read()

        # Установка соединения с сервером minio-grpc
        channel = grpc.insecure_channel('localhost:50051')
        stub = MinioServiceStub(channel)

        # Отправляем запрос на загрузку объекта
        response = stub.UploadObject(minio_service_pb2.UploadObjectRequest(
            bucket_name=bucket_name,
            object_name=object_name,
            file_content=file_content
        ))

        # Формируем и возвращаем ответ в формате JSON:
        return JsonResponse({
            'success': response.success,
            'error_message': response.message_error
        })