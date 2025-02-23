# 361microserviceA
361 microservice A 
A.	Requesting Data:
Please run random_date_service.py in a terminal and then to call the service create a zmq socket connection to port 6666 and send a request and then decode the response. 
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:6666")
        socket.send_string("Please Send Random Date")

B.	Receiving Data
After sending the request the random_date_service will send a response. Please call the recv.() and also .decode() in order to get the random date. 

        Rando_date = socket.recv()

C.	UML
 ![microAuml drawio](https://github.com/user-attachments/assets/d4d9c86f-5b0c-41b9-9d38-555e18fad854)
