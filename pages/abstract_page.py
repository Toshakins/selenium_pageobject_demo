class AbstractPage:
    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver