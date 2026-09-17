# 9.	Create an abstract class CloudStorage with abstract methods:
# a)	upload_file() 
# b)	download_file() 
# c)	delete_file() 
# Create subclasses representing different storage services and implement the operations.

from abc import ABC, abstractmethod

class CloudStorage(ABC):
    def __init__(self, service_name):
        self.service_name = service_name
        self.storage = set()

    @abstractmethod
    def upload_file(self, filename):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass


class GoogleDrive(CloudStorage):
    def __init__(self):
        super().__init__("Google Drive")

    def upload_file(self, filename):
        self.storage.add(filename)
        print(f"[{self.service_name}] Uploaded '{filename}' to Google Workspace Cloud Drive.")

    def download_file(self, filename):
        if filename in self.storage:
            print(f"[{self.service_name}] Fetching '{filename}' via Google Drive REST API...")
        else:
            print(f"[{self.service_name}] 404: '{filename}' not found.")

    def delete_file(self, filename):
        if filename in self.storage:
            self.storage.remove(filename)
            print(f"[{self.service_name}] Moved '{filename}' to Trash Bin.")
        else:
            print(f"[{self.service_name}] File not found to delete.")


class AWSS3(CloudStorage):
    def __init__(self, bucket_name="apc-bucket-2026"):
        super().__init__("AWS S3")
        self.bucket_name = bucket_name

    def upload_file(self, filename):
        self.storage.add(filename)
        print(f"[{self.service_name}] PutObject: '{filename}' pushed to S3 bucket '{self.bucket_name}'.")

    def download_file(self, filename):
        if filename in self.storage:
            print(f"[{self.service_name}] GetObject: Streaming '{filename}' from bucket '{self.bucket_name}'.")
        else:
            print(f"[{self.service_name}] NoSuchKey: '{filename}' does not exist in bucket.")

    def delete_file(self, filename):
        if filename in self.storage:
            self.storage.remove(filename)
            print(f"[{self.service_name}] DeleteObject: '{filename}' permanently purged from '{self.bucket_name}'.")
        else:
            print(f"[{self.service_name}] Object not found.")


providers = [GoogleDrive(), AWSS3()]

print("Cloud Storage Abstract Operations")
for provider in providers:
    provider.upload_file("dataset.parquet")
    provider.download_file("dataset.parquet")
    provider.delete_file("dataset.parquet")
    print("-" * 40)
