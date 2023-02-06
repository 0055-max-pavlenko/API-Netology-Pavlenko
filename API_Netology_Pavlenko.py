
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    

    def _get_upload_link(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type':'application/json',
            'Authorization':'OAuth {}'.format(self.token)
            }
        params = {"path":file_path, "overwrite":"true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, file_path, file_name):
        href = self._get_upload_link(file_path=file_path).get("href","")
        response = requests.put(href, data=open(file_name,'rb'))
        return response


if __name__ == '__main__':
    
    path_to_file = input('Введите путь до файла:')
    token = input('Введите токен:')
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(file_path="Загрузки/test0055.txt", file_name=path_to_file)
    
    if result.status_code == 201:
        print('Файл успешно загружен')
    else:
        print(f'Загрузка файла неуспешна, ответ сервера {result.status_code}')