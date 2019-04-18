import load_data
from Network import Network

training_data, validation_data, test_data = load_data.load_data_wrapper()

net = Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)