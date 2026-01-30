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

        # init
        self.car_id = ac.getFocusedCar()

        # labels
        self.labels = [
            Label(app_window, self.car_id, xPos, yPos, metric)
            for xPos, yPos, metric in [
                (0, 30, acsys.CS.SpeedKMH),
                (0, 60, acsys.CS.SlipRatio),
                (0, 90, acsys.CS.SlipAngle),
                (0, 120, acsys.CS.LocalVelocity),
            ]
        ]

    def on_acUpdate(self, dt: int) -> None:
        # display telemetry
        for label in self.labels:
            label.display()
