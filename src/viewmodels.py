from services import DataService
from di_builder import di


class HomeViewModel:
    def __init__(self, data_service: DataService) -> None:
        self.data_service = data_service
        self.data: str = "data"
        self.sdata: int = self.data_service.provide_data()

        return

    def command_operation(self) -> None:
        self.data_service.launch_operation()
        return None


di.add_singleton(HomeViewModel)
