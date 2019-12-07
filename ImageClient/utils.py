import requests
from requests_html import HTMLSession

session = HTMLSession()

server_base_url = "http://localhost:50610/Home/Images"
server_download_url = "http://localhost:50610/Content/images"
local_folder = "images"


def get_server_image(img_name):
    url = f"{server_base_url}/?name={img_name}"
    imgElement = None
    try:
        r = session.get(url)
        imgElement = r.html.find("img", first=True)
    except Exception as e:
        print(e)
        r.close()
    finally:
        r.close()
    return imgElement


def download_image(img_name, ext="jpg"):
    local_path = f"{local_folder}\{img_name}_copy.{ext}"
    url = f"{server_download_url}/{img_name}.{ext}"
    rv = True
    r = requests.get(url)
    try:
        with open(local_path, "wb") as f:
            f.write(r.content)
    except Exception as e:
        print(e)
        rv = False
    finally:
        r.close()
    return rv

