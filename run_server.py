from services.server import createServer


if __name__ == '__main__':
    app = createServer()
    app.run(port=8080)

