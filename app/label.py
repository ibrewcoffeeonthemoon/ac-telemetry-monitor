import ac


class Label:
    def __init__(
        self,
        app_window: int,
        car_id: int,
        xPos: int,
        yPos: int,
        metric: int,
    ) -> None:
        self._label = ac.addLabel(app_window, '')
        self._car_id = car_id
        self._metric = metric
        ac.setPosition(self._label, xPos, yPos)

    def set_text(self, txt: str) -> None:
        ac.setText(self._label, txt)

    def display(self) -> None:
        val = ac.getCarState(self._car_id, self._metric)
        if isinstance(val, tuple):
            txt = ' '.join(['{: >+10.4f}'.format(v) for v in val])
        else:
            txt = '{: >+10.4f}'.format(val)
        ac.setText(self._label, txt)
