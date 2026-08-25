class Logger:

    def __init__(self):
        self.time = {}


        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
        if message in self.time:
            prev = self.time[message]
            if timestamp - prev >= 10:
                self.time[message] = timestamp
                return True
            else:
                return False
        else:
            self.time[message] = timestamp
        return True





