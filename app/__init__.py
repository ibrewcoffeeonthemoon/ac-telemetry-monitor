import sys

import ac
import acsys

from app.label import Label


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

        # labels
        self.label_SpeedKMH = Label(app_window, 3, 30)
        self.label_SlipRatio = Label(app_window, 3, 60)

        # init
        self.car_id = ac.getFocusedCar()

    def on_acUpdate(self, dt: int) -> None:
        # resolve speed
        speed_kmh = ac.getCarState(self.car_id, acsys.CS.SpeedKMH)
        slip_ratio = ac.getCarState(self.car_id, acsys.CS.SlipRatio)

        # display telemetry
        self.label_SpeedKMH.set_text('Speed: {:.0f}'.format(speed_kmh))
        self.label_SlipRatio.set_text('SlipRatio: {:.4f}, {:.4f}, {:.4f}, {:.4f}'.format(*slip_ratio))
