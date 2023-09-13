from di_builder import di


class DataService:
    def __init__(self) -> None:
        return

    def provide_data(self) -> int:
        return 2

    def launch_operation(self) -> None:
        print("Operation....")
        return None


di.add_transient(DataService)
