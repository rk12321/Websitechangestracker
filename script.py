import requests
import io

url = 'https://www.carandbike.com';
html_output_name = 'carnbikeafter.txt';

req = requests.get(url, 'html.parser')


with io.open(html_output_name, "w", encoding="utf-8") as f:
    f.write(req.text)
