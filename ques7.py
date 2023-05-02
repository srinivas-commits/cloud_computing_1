from zeep import Client

# create a client using the WSDL document
client = Client('http://localhost:8000/?wsdl')

# print the available service operations
print(client.service)

# call a service operation
result = client.service.say_hello('Anand')

# print the result
print(result)
