from webdav3.client import Client
from auth import data


def webdav_list():
    client = Client(data)
    print(client.list())


def webdav_upload():
    client = Client(data)

    if not client.check("backup/1"):
        client.mkdir("backup/1")

    client.upload("backup/1",
                  "/Users/AlexKAD/Projects/python/cloud-mail-webdav/test-upload")


if __name__ == '__main__':
    webdav_upload()
    webdav_list()