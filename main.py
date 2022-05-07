import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    #получаем ссылку для загрузки
    def _get_upload_link(self,name_file,upload_url):
        headers = self.get_headers()
        params = {"path": name_file,"overwrite": "true"}
        resp = requests.get(upload_url,headers=headers,params=params)
        return resp.json()

    #загружаем файл
    def upload(self, file_path: str, file_name: str, host: str):
        href_json = self._get_upload_link(name_file=file_name,upload_url=host)
        href = href_json["href"]
        resp = requests.put(href,data=open(file_path,'rb'))
        return resp.status_code


if __name__ == '__main__':
    TOKEN = ''
    name_file = "doc_upload.txt"
    path_to_file_to_pc = 'N:\doc_upload.txt'
    host_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    YaLoad = YaUploader(token=TOKEN)
    Status = YaLoad.upload(path_to_file_to_pc,name_file,host_upload)
    if Status == 201:
        print("Всё успешно!")