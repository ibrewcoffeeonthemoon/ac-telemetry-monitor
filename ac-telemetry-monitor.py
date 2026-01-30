from app import App


def acMain(ac_version: str) -> str:
    # create app
    global app
    app = App(
        name='AC Telemetry Monitor',
        width=400,
        height=200,
        ac_version=ac_version
    )

    # app name
    return app.name


def acUpdate(dt: int) -> None:
    # on update
    global app
    app.on_acUpdate(dt)
