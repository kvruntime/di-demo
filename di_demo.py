# pip install python-injection
# pip install simple-injection
# from simple_injection import ServiceCollection
from di_builder import di


class DataService:
    def __init__(self) -> None:
        return

    def provide_data(self) -> int:
        return 2


class HomeViewModel:
    def __init__(self, data_service: DataService) -> None:
        self.data_service = data_service
        self.data: str = "data"
        self.sdata: int = self.data_service.provide_data()
        return


class HomePage:
    def __init__(self, vm: HomeViewModel) -> None:
        self.vm = vm
        return

    def print_data(self) -> None:
        print(f"data: {self.vm.data}")
        return None

    def print_sdata(self) -> None:
        print(f"sdata: {self.vm.sdata}")
        return None


di.add_singleton(DataService)
di.add_transient(HomeViewModel)
di.add_singleton(HomePage)
