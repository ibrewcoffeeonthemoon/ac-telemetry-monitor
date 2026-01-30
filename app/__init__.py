import sys

import ac
import acsys


class App:
    def __init__(
        self,
        name: str,
        width: int,
        height: int,
        ac_version: str,
    ) -> None:
        self.name = name
        self.width = width
        self.height = height
        self.ac_version = ac_version

        # create app window
        app_window = ac.newApp(self.name)

        # size
        ac.setSize(app_window, self.width, self.height)

        # print version info
        msg = '{name}: App: ac v{ac_version}, python v{py_version}'.format(
            name=self.name,
            py_version=sys.version,
            ac_version=self.ac_version
        )
        ac.log(msg)
        ac.console(msg)

        # label
        self.label = ac.addLabel(app_window, '')
        ac.setPosition(self.label, 3, 30)

        # init
        self.focused_car_id = ac.getFocusedCar()

    def on_acUpdate(self, dt: int) -> None:
        # resolve speed
        speed_kmh = ac.getCarState(self.focused_car_id, acsys.CS.SpeedKMH)

        # display telemetry
        ac.setText(self.label, 'Speed: {speed:.0f}'.format(speed=speed_kmh))
