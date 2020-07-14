from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
import sys
import json

from weatherDesign import Ui_MainWindow
from Network import Network
from getImage import getImage


class Main(Ui_MainWindow, QMainWindow):
    net = Network()

    def __init__(self):
        super(Main, self).__init__()

        self.setupUi(self)
        self.addHandlers()

    def addHandlers(self):
        # start load data
        self.city.returnPressed.connect(self.loadInfo)

    def loadInfo(self):
        print(self.city.text())
        city = self.city.text()

        self.setWindowTitle(f"Weather App - {city}")

        self.startLoading()

        # make requests
        self.net.getToday(city, self.changeToday, self.showError)

    def startLoading(self):
        self.loadLabel.show()

    def finishLoading(self):
        self.loadLabel.hide()

    def changeToday(self, data):
        jsonData = json.loads(data)

        if int(jsonData['cod']) != 200:
            self.showError(jsonData['message'])
            return

        # change image
        weatherID = int(jsonData['weather'][0]['id'])

        self.todayImg.setPixmap(QPixmap(f"images/weatherTypes/{getImage(weatherID)}"))
        self.todayImg.setToolTip(jsonData['weather'][0]['main'])

        # change labels
        self.todayTemp.setText(str(jsonData['main']['temp']))
        self.todayHumidity.setText(str(jsonData['main']['humidity']))
        self.todayPressure.setText(str(jsonData['main']['pressure']))

        # request week weather
        self.net.getWeek(jsonData['name'], self.changeWeek, self.showError)

    def changeWeek(self, data):
        jsonData = json.loads(data)

        if int(jsonData['cod']) != 200:
            self.showError(jsonData['message'])
            return

        # filter weather data
        daysWeather = list(filter(lambda item: item['dt_txt'].endswith('18:00:00'), jsonData['list']))
        print(daysWeather)

        for i in range(1, 6):
            weatherID = int(daysWeather[i - 1]['weather'][0]['id'])

            pixmap = QPixmap(f"images/weatherTypes/{getImage(weatherID)}")
            getattr(self, f"img_{i}").setPixmap(pixmap)
            getattr(self, f"img_{i}").setToolTip(daysWeather[i - 1]['weather'][0]['main'])

            getattr(self, f"temp_{i}").setText(str(daysWeather[i - 1]['main']['temp']))
            getattr(self, f"humidity_{i}").setText(str(daysWeather[i - 1]['main']['humidity']))
            getattr(self, f"pressure_{i}").setText(str(daysWeather[i - 1]['main']['pressure']))

        self.finishLoading()

    def showError(self, error: str):
        QMessageBox.warning(self, 'Error in request', error)

        self.finishLoading()


app = QApplication(sys.argv)
main = Main()
main.show()

sys.exit(app.exec_())
