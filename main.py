import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_lable = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_lable = QLabel(self)
        self.emoji_lable = QLabel(self)
        self.description = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("A weather app")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_lable)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_lable)
        vbox.addWidget(self.emoji_lable)
        vbox.addWidget(self.description)

        self.setLayout(vbox)

        self.city_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperature_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emoji_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.city_lable.setObjectName("city_lable")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_lable.setObjectName("temperature_lable")
        self.emoji_lable.setObjectName("emoji_lable")
        self.description.setObjectName("description")


        self.setStyleSheet("""

            QLabel, QPushButton{
                         font_family: calibri;  
                           }

            QLabel#city_lable{
                        font-size: 40px;
                        font-style: italic;   
                           }

            QLineEdit#city_input{
                        font-size: 40px;   
                           }    

            QPushButton#get_weather_button{
                        font-size: 30px;
                        font-weight: bold;
                           } 

            QLabel#temperature_lable{
                        font-size: 70px;       
                           }   

            QLabel#emoji_lable{
                        font-size: 100px;
                        font-family: segoe UI emoji; 
                           }    

            QLabel#description{
                        font-size: 50px;
                           }             
                        
                                """)
        

        self.get_weather_button.clicked.connect(self.get_weather)        

    def get_weather(self):
        API_key = "51caea943451d3c1b7b0c84ed5f444f8"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal server error:\nPlease try again later")
                case 502:
                    self.display_error("Bad gateway:\nInvalid request from server")
                case 503:
                    self.display_error("Service unavailable:\nServer is down")
                case 504:
                    self.display_error("Gaitway timer:\nNo response from server")
                case _:
                    self.display_error(f"HTTP error occoured:\n{http_error}")
                
        except requests.exceptions.ConnectionError:
            self.display_error("connection error:\nCheck your Internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Time out error:\nThe request timeout")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nCheck the Url")
        except requests.exceptions.RequestException as request_error:
            self.display_error(f"Request error:\n{request_error}")

    def display_error(self, message):
        self.temperature_lable.setStyleSheet("font-size: 30px;")
        self.temperature_lable.setText(message)
        self.emoji_lable.clear()
        self.description.clear()

    def display_weather(self, data):
        self.temperature_lable.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]


        self.temperature_lable.setText(f"{temperature_c:.0f}°C")
        self.emoji_lable.setText(self.get_weather_emoji(weather_id))
        self.description.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        
        if 200 <= weather_id <= 232:
            return "🌩️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "😶‍🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🌊"
        elif weather_id == 701:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())