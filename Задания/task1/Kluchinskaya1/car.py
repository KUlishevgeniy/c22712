import time
class Car:
  def __init__(self, model, color, volume):
    self.model = model
    self.color = color
    self.volume = volume
  def print(self):
    print(self.model, self.color, self.volume)

  def start(self):
    self.start_time = int(time.time())

  def stop(self):
    self.volume -= int(time.time()) - self.start_time
obj = Car("test","test1",5)
obj.print()
obj.start()
time.sleep(2)
obj.stop()
obj.print()