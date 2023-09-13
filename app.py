from di_builder import di

from di_demo import HomePage


class Application:
    def __init__(self) -> None:
        page = di.resolve(HomePage)
        page.print_data()
        page.print_sdata()


di.add_singleton(Application)
