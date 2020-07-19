from pyfirmata import Arduino, util
import time
board = Arduino('COM3')






iterator = util.Iterator(board)
iterator.start()

Tv1 = board.get_pin('a:0:1')
time.sleep(1.0)
print(Tv1.read())


time.sleep(1.0)
print(Tv1.read())



time.sleep(1.0)
print(Tv1.read())