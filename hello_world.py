from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class HelloWorldService(ServiceBase):
    @rpc(str, _returns=str)
    def say_hello(ctx, name):
        return "Hello, %s!" % name


application = Application([HelloWorldService], tns='spyne.examples.hello', in_protocol=Soap11(), out_protocol=Soap11())

if __name__ == '__main__':
    wsgi_application = WsgiApplication(application)
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    server = make_server('localhost', 8000, wsgi_application)
    server.serve_forever()
