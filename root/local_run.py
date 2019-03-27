# run server localy
from root.app import app

if __name__ == '__main__':
    app.Debug = True
    app.run()
