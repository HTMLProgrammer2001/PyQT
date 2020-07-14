from PyQt5.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager
from PyQt5.QtCore import QUrl


class Network:
    key = '37d34c5ad2416876ed7bded854432e17'
    url = 'http://api.openweathermap.org/data/2.5'

    def __init__(self):
        # request callbacks
        self.successCallback = lambda data: print(data)
        self.errorCallback = lambda error: print(error)

        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.getResult)

    def getResult(self, reply: QNetworkReply):
        error = reply.error()

        # request was successfully made
        if error == QNetworkReply.NoError:
            data = reply.readAll()
            self.successCallback(str(data, 'utf-8'))
        else:
            # request was failed
            errorStr = reply.errorString()
            self.errorCallback(errorStr)

    def getToday(self, city, success, error):
        self.successCallback = success
        self.errorCallback = error

        url = QUrl(f"{self.url}/weather?q={city}&appid={self.key}&units=metric")
        req = QNetworkRequest(url)
        self.manager.get(req)

    def getWeek(self, city, success, error):
        self.successCallback = success
        self.errorCallback = error

        url = QUrl(f"{self.url}/forecast?q={city}&appid={self.key}&units=metric")
        req = QNetworkRequest(url)
        self.manager.get(req)
