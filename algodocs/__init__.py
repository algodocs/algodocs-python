import requests
from json import loads

__author__ = "Ibrahim Nalbant"
__contact__ = "support@algodocs.com"
__date__ = "7/27/2022"
__version__ = 1.0

class AlgoDocsClient:
    """
    Python client for AlgoDocs API (https://api.algodocs.com)
    """
    def __init__(self, email_address, key):
        """
        AlgoDocsClient constructor
        """
        self.BASE_URL = "https://api.algodocs.com/v1"
        self.KEY = key
        self.EMAIL = email_address
        self.AUTH = (self.EMAIL, self.KEY)

    def me(self):
        """
        tests authentication
        returns your name and surname with email address you registered at AlgoDocs
        """
        result = requests.get(self.BASE_URL + "/me", auth=self.AUTH)
        if result.status_code == 200:
            return loads(result.text)
        return result.reason

    def getExtractors(self):
        """
        retrieves all extractors
        """
        result = requests.get(self.BASE_URL + "/extractors", auth=self.AUTH)
        if result.status_code == 200:
            return loads(result.text)
        return result.reason
    
    def getFolders(self):
        """
        retrieves all folders
        """
        result = requests.get(self.BASE_URL + "/folders", auth=self.AUTH)
        if result.status_code == 200:
            return loads(result.text)
        return result.reason
    
    def uploadDocumentLocal(self, extractor_id, folder_id, file_path):
        """
        uploads a document from a given file path for extractor_id and folder_id
        """
        try:
            file = open(file_path, "rb")
        except FileNotFoundError:
            return "Failed to read file"

        result = requests.post(
            self.BASE_URL + "/document/upload_local/" + extractor_id + "/" + folder_id,
            auth=self.AUTH,
            files={"file": file}
        )

        if result.status_code == 200:
            return loads(result.text)
        return result.reason

    def uploadDocumentUrl(self,extractor_id, folder_id, url):
        """
        uploads a document from a publicly accessible url for extractor_id and folder_id
        """
        payload = {
            "url": url
            }
    
        result = requests.post(self.BASE_URL + "/document/upload_url/" + extractor_id+"/"+ folder_id,payload,auth=self.AUTH)
        if result.status_code == 200:
            return loads(result.text)
        return result.reason
    
    def uploadDocumentBase64(self, extractor_id, folder_id, file_base64, file_name):
        """
        uploads a document in base64 format for extractor_id and folder_id using the passed file_name
        """
        payload = {
            "file_base64": file_base64,
            "filename": file_name
            }
        result = requests.post(self.BASE_URL + "/document/upload_base64/" + extractor_id + "/" + folder_id, payload, auth=self.AUTH)
        if result.status_code == 200:
            return loads(result.text)
        return result.reason
    
    def getExtractedDataByDocumentID(self, document_id):    
        """
        retrieves extracted data of a single document by document_id
        """
        result = requests.get(self.BASE_URL + "/extracted_data/" + document_id,auth=self.AUTH)
        if result.status_code == 200:
            return loads(result.text)
        return result.reason
    
    def getExtractedDataByExtractorID(self, extractor_id, folder_id = None, limit = 100, date = None):
        """
        retrieves extracted data of multiple documents by extractor_id
        optional parameters: folder_id, limit (default 100) and date
        """
        payload = {
            "folder_id": folder_id,
            "date": date,
            "limit": limit
        }        
        result = requests.get(self.BASE_URL + "/extracted_data/" + extractor_id, payload, auth=self.AUTH)
        if result.status_code == 200:
            return loads(result.text)
        return result.reason