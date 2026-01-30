from typing import Any, Callable


def addButton(object: Any, text: str) -> int:
    ...


def addCheckBox(object: Any, title: str) -> int:
    ...


def addGraph(object: Any, title: str) -> int:
    ...


def addItem(object: Any, name: str) -> int:
    ...


def addLabel(window: Any, name: str) -> int:
    ...


def addListBox(object: Any, title: str) -> int:
    ...


def addOnAppActivatedListener(object: Any, function: Callable) -> int:
    ...


def addOnAppDismissedListener(object: Any, function: Callable) -> int:
    ...


def addOnChatMessageListener(object: Any, function: Callable) -> int:
    ...


def addOnCheckBoxChanged(object: Any, function: Callable) -> int:
    ...


def addOnClickedListener(object: Any, function: Callable) -> int:
    ...


def addOnListBoxDeselectionListener(object: Any, function: Callable) -> int:
    ...


def addOnListBoxSelectionListener(object: Any, function: Callable) -> int:
    ...


def addOnValidateListener(object: Any, function: Callable) -> int:
    ...


def addOnValueChangeListener(object: Any, function: Callable) -> int:
    ...


def addProgressBar(object: Any, title: str) -> int:
    ...


def addRenderCallback(object: Any, function: Callable) -> int:
    ...


def addSerieToGraph(object: Any, r: float, g: float, b: float) -> int:
    ...


def addSpinner(object: Any, title: str) -> int:
    ...


def addTextBox(object: Any, title: str) -> int:
    ...


def addTextInput(object: Any, text: str) -> int:
    ...


def addValueToGraph(object: Any, serieId: int, value: float) -> int:
    ...


def console(msg: str) -> int:
    ...


def drawBackground(object: Any, visibility: bool) -> int:
    ...


def drawBorder(object: Any, visibility: bool) -> int:
    ...


def freeCameraMoveForward(self) -> int:
    ...


def freeCameraMoveRight(self) -> int:
    ...


def freeCameraMoveUpWorld(self) -> int:
    ...


def freeCameraRotateHeading(self) -> int:
    ...


def freeCameraRotatePitch(self) -> int:
    ...


def freeCameraRotateRoll(self) -> int:
    ...


def freeCameraSetClearColor(self) -> int:
    ...


def getCameraMode(self) -> int:
    ...


def getCarLeaderboardPosition(carId: int) -> int:
    ...


def getCarMinHeight(carId: int) -> float:
    ...


def getCarName(carId: int) -> str:
    ...


def getCarRealTimeLeaderboardPosition(carId: int) -> int:
    ...


def getCarState(carId: int, infoId: int, param: str = "") -> Any:
    ...


def getCarsCount(self) -> int:
    ...


def getCurrentSplits(carId: int) -> tuple[float, float, float]:
    ...


def getDriverName(carId: int) -> str:
    ...


def getFocusedCar() -> int:
    ...


def getItemCount(object: Any) -> int:
    ...


def getLastSplits(carId: int) -> tuple[float, float, float]:
    ...


def getPosition(object: Any) -> tuple[float, float]:
    ...


def getSelectedItems(object: Any) -> int:
    ...


def getSize(object: Any) -> tuple[int, int]:
    ...


def getText(object: Any) -> str:
    ...


def getTrackConfiguration(carId: int) -> str:
    ...


def getTrackName(carId: int) -> str:
    ...


def getValue(object: Any) -> int:
    ...


def glBegin(drawType: int) -> int:
    ...


def glColor3f(r: float, g: float, b: float) -> int:
    ...


def glColor4f(r: float, g: float, b: float, a: float) -> int:
    ...


def glEnd(self) -> int:
    ...


def glQuad(xPos: float, yPos: float, width: float, height: float) -> int:
    ...


def glQuadTextured(xPos: float, yPos: float, width: float, height: float, texId: int) -> int:
    ...


def glVertex2f(xPos: float, yPos: float) -> int:
    ...


def highlightListBoxItem(object: Any, id: int) -> int:
    ...


def isAcLive(self) -> bool:
    ...


def isCameraOnBoard(self) -> bool:
    ...


def log(msg: str) -> int:
    ...


def newApp(appName: str) -> int:
    ...


def newTexture(path: str) -> int:
    ...


def removeItem(object: Any, id: int) -> int:
    ...


def sendChatMessage(msg: str) -> int:
    ...


def setAllowDeselection(object: Any, allow: bool) -> int:
    ...


def setAllowMultiSelection(object: Any, allow: bool) -> int:
    ...


def setBackgroundColor(object: Any, r: float, g: float, b: float) -> int:
    ...


def setBackgroundOpacity(object: Any, opacity: float) -> int:
    ...


def setBackgroundTexture(object: Any, texture: str) -> int:
    ...


def setCameraMode(mode: int) -> int:
    ...


def setFocus(object: Any, focus: bool) -> int:
    ...


def setFont(object: Any, font: str) -> int:
    ...


def setFontAlignment(object: Any, alignment: int) -> int:
    ...


def setFontColor(object: Any, r: float, g: float, b: float, a: float) -> int:
    ...


def setFontSize(object: Any, size: float) -> int:
    ...


def setIconPosition(object: Any, xPos: float, yPos: float) -> int:
    ...


def setItemNumberPerPage(object: Any, numItems: int) -> int:
    ...


def setPosition(object: Any, xPos: float, yPos: float) -> int:
    ...


def setRange(min: float, max: float, maxPoint: float = 0.0) -> int:
    ...


def setSize(object: Any, width: int, height: int) -> int:
    ...


def setStep(object: Any, step: float) -> int:
    ...


def setText(object: Any, text: str) -> int:
    ...


def setTitle(object: Any, title: str) -> int:
    ...


def setTitlePosition(object: Any, xPos: float, yPos: float) -> int:
    ...


def setValue(object: Any, value: float) -> int:
    ...


def setVisible(object: Any, visible: bool) -> int:
    ...
