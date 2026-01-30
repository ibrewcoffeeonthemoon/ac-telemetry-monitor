import sys

import ac
import acsys

APP_NAME = 'AC-Telemetry-Monitor'
WIDTH, HEIGHT = 400, 200


def acMain(ac_version: str) -> str:
    # create app window
    app_window = ac.newApp(APP_NAME)

    # size
    ac.setSize(app_window, WIDTH, HEIGHT)

    # print version info
    msg = '{name}: Hello, ac v{ac_version}, python v{py_version}'.format(
        name=APP_NAME,
        py_version=sys.version,
        ac_version=ac_version
    )
    ac.log(msg)
    ac.console(msg)

    # label
    label = ac.addLabel(app_window, 'Label: This is a label')
    ac.setPosition(label, 3, 30)

    # app name
    return APP_NAME
