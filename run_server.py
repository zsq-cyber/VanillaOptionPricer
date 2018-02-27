from services.server import create_server


if __name__ == '__main__':
    app = create_server()
    app.run(port=8080)

