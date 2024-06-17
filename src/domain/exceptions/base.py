class BaseAppException(Exception):
    def __init__(self, message: str = "Application occured exception"):
        self.message = message
        super().__init__(message)
