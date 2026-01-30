import ac


class Label:
    def __init__(
        self,
        app_window: int,
        xPos: int,
        yPos: int,
        init_txt: str = '',
    ) -> None:
        self._label = ac.addLabel(app_window, init_txt)
        ac.setPosition(self._label, xPos, yPos)

    def set_text(self, txt: str) -> None:
        ac.setText(self._label, txt)
