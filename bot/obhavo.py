import requests
from pprint import pprint as print
from googletrans import Translator

translator = Translator()
def data(obhavo):
    api_key = 'aaa299a8f90c1ee6a718bbd0232d52c1'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={obhavo}&units=metric&appid={api_key}'
    r = requests.get(url)
    res = r.json()
    if r.status_code == 200:
        output = {"icon": res["weather"][0]['icon'], "joy": res["name"], "havo": res["main"]["temp_min"], "dav": res["sys"]["country"], "ob": res["weather"][0]["description"]}
        return output
    else:
        return False

if __name__ == '__main__':
    from pprint import pprint as print
    print(data('amazon'))

