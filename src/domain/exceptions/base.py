class BaseAppException(Exception):
    def __init__(self, message: str = "Application occured exception"):
        super().__init__(message)
