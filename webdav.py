from webdav3.client import Client
from auth import data


def webdav_list():
    client = Client(data)
    print(client.list())


if __name__ == '__main__':
    webdav_list()