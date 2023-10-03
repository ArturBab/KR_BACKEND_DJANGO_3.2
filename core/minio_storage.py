from storages.backends.s3boto3 import S3Boto3Storage


class MinioStorage(S3Boto3Storage):
    location = 'kursach4-backend-test1'
    default_acl = 'public-read'
