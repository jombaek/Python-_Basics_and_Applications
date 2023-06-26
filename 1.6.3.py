class LoggableList(list, Loggable):
    def append(self, item):
        super(LoggableList, self).append(item)
        self.log(item)