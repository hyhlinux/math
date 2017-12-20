import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.httpclient import AsyncHTTPClient
from tornado import gen
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class AsyncHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        resp = yield http_client.fetch("http://example.com")
        print(resp)
        self.write("{}".format(resp))


class AsyncDictHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        resp_dict = yield dict(
            resp1=http_client.fetch("http://example.com"),
            resp2=http_client.fetch("http://example.com"),
        )
        print(resp_dict)
        self.write("{}".format(resp_dict))


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello')


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/aio", AsyncHandler),
        (r"/aiodict", AsyncDictHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
