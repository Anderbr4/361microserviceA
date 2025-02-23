import unittest
import zmq

from random_date_service import (
    generate_random_date
)




class TestAddFunction(unittest.TestCase):
    def test_generate_date_time_1(self):
        context = zmq.Context()

        socket = context.socket(zmq.REQ)

        socket.connect("tcp://localhost:6666")

        print("Getting Random Date For Test One")

        socket.send_string("Please Send Random Date")

        message = socket.recv()

        print(f"We got date: {message.decode()}")

        socket.send_string("Quit") 

        context.destroy()

        self.assertTrue(len(message) > 0)





if __name__ == '__main__':
    unittest.main()