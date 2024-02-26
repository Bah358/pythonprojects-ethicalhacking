import weattherinfolib


if __name__ == "__main__":
    test1=weattherinfolib.weatherinfo()
    test1.loadLocations()
    test1.sendWeatherInfo()