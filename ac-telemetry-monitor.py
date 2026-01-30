import ac
import acsys

APP_NAME = 'AC-Telemetry-Monitor'
WIDTH, HEIGHT = 400, 200


def acMain(ac_version):
    appWindow = ac.newApp(APP_NAME)

    ac.setSize(appWindow, WIDTH, HEIGHT)

    ac.log("Hello, Assetto Corsa application world!")
    ac.console("Hello, Assetto Corsa console!")

    return APP_NAME
