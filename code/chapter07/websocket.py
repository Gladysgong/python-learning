import Tornados.ioloop
import Tornados.web
import Tornados.websocket

from Tornados.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)

# we gonna store clients in dictionary..
clients = dict()


class IndexHandler(Tornados.web.RequestHandler):
    @Tornados.web.asynchronous
    def get(self):
        #self.write("This is your response")
        # self.finish()
        self.render("index.html")


class WebSocketHandler(Tornados.websocket.WebSocketHandler):
    def open(self, *args):
        self.id = self.get_argument("Id")
        self.stream.set_nodelay(True)
        clients[self.id] = {"id": self.id, "object": self}

    def on_message(self, message):
        """
        when we receive some message we want some message handler..
        for this example i will just print message to console
        """
        print("Client %s received a message : %s" % (self.id, message))

    def on_close(self):
        if self.id in clients:
            del clients[self.id]
            print("Client %s is closed" % (self.id))


app = Tornados.web.Application([
    (r'/', IndexHandler),
    (r'/websocket', WebSocketHandler),
])

import threading
import time


def sendTime():
    import datetime
    while True:
        for key in clients.keys():
            msg = str(datetime.datetime.now())
            clients[key]["object"].write_message(msg)
            print("write to client %s: %s" % (key, msg))
        time.sleep(1)


if __name__ == '__main__':
    threading.Thread(target=sendTime).start()
    parse_command_line()
    app.listen(options.port)
    Tornados.ioloop.IOLoop.instance().start()
