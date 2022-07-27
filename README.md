## AlgoDocs API Python Client

This client API provides all required Python bindings for communicating with [AlgoDocs REST API](https://api.algodocs.com).

## Documentation

Please visit [AlgoDocs API Documentation](https://api.algodocs.com/) for a detailed documentation of all API methods with their parameters and expected responses.

## Installation

**Using pip**:

**Note:** algodocs python client was only tested with Python 3.

`pip install algodocs`

**OR**

Clone current repository or download as zip file and unzip its contents, then change directory to the root folder and then install.

`git clone https://github.com/algodocs/algodocs-python` <br>
`cd algodocs-python` <br>
`python setup.py install` <br>

__**For development:**__
`pip install -r requirements.txt`

## Usage

To use AlgoDocs Python Client, you need to register at [AlgoDocs](https://algodocs.com) and get your API Key from [here](https://app.algodocs.com/restapi)

```python
import algodocs

email_address = "your_email_addres_you_registered_with_at_AlgoDocs"
key = "your_secret_api_key"
client = algodocs.AlgoDocsClient(email_address, key)
```

Test connection and authenticate as follows:
```python
result = client.me()
print(result) #this will print your name, surname and email address
```

Get all extractors in your AlgoDocs account:
```python
result = client.getExtractors()
print(result)
```

Get all folders in your AlgoDocs account:
```python
result = client.getFolders()
print(result)
```

Upload local file using its full path:
```python
file_path= "full_path_to_your_file.pdf" #accepted file types: PDF, PNG, JPG/JPEG, WORD (.doc, .docx), EXCEL (.xls, .xlsx)
extractor_id = "your_extractor_id" #use extractor id that you got from client.getExtractors()
folder_id = "your_folder_id" #use folder id that you got from client.getFolders()

result=client.uploadDocumentLocal(extractor_id, folder_id, file_path)
print(result)
```

Upload file in base64 format:
```python
with open(file_path, "rb") as file_contents:
   file_base64 = base64.b64encode(file_contents.read())
   result=client.uploadDocumentBase64(extractor_id, folder_id, file_base64, os.path.basename(file_path))
   print(result)
```

Upload file using its publicly accessible url:
```python
url="https://api.algodocs.com/content/SampleInvoice.pdf"

result=client.uploadDocumentUrl(extractor_id, folder_id, url)
print(result)
```

Get extracted data of a single document using its id:
```python
document_id="your_document_id" #this document_id comes from result['id'] above, so use your actual document_id that you received in response dictionary object after importing the document to AlgoDocs...
result=client.getExtractedDataByDocumentID(document_id)
print(result)
```

Get extracted data of multiple documents using extractor id:
```python
#`folder_id`, `limit` and `date` parameters are optional
limit = 10
date = (datetime.now() + timedelta(days=-10)).isoformat() # i.e. get extracted data from documents that were uploaded during last 10 days
result=client.getExtractedDataByExtractorID(extractor_id, folder_id, limit, date)
print(result)
```
<br>

#### Contributing

Bug reports and pull requests are welcome on [GitHub](https://github.com/algodocs/algodocs-python).

<br>

#### License

The library is available as open source under the terms of the [MIT License](https://github.com/algodocs/algodocs-python/blob/master/LICENSE.txt).

<br>

### MIT License

_Copyright (c) 2022 Algosoft Ltd._

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.