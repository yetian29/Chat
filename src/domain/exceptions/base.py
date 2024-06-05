class BaseApplicationException(Exception):
    @property
    def message(self):
        return "Application exception occured"
