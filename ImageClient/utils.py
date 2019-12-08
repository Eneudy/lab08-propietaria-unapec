import requests
from requests_html import HTMLSession

session = HTMLSession()

server_base_url = "http://localhost:50610" 
server_image_url = f"{server_base_url}/Home/Images"
server_download_url = f"{server_base_url}/Content/images"
local_img_folder = "images"


class ImageClient(object):

    @staticmethod
    def get_server_image(img_name):
        url = f"{server_image_url}/?name={img_name}"
        r = session.get(url)
        imgElement = r.html.find("img", first=True)
        return imgElement

    @staticmethod
    def download_image(img_name, ext="jpg"):
        filename = f"{local_img_folder}\{img_name}_copy.{ext}"
        url = f"{server_download_url}/{img_name}.{ext}"
        r = requests.get(url)
        with open(filename, "wb") as f:
            f.write(r.content)
        return True
