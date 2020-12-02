import logging

from aiohttp import web

from proxy.routes import routes


def main():
    logging.basicConfig(level=logging.DEBUG)

    app = web.Application()
    app.router.add_routes(routes)
    web.run_app(app)


if __name__ == '__main__':
    main()
