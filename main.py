from flask import Flask, session
from flask_cors import CORS
from flask_session import Session
from userService import user_service
import cryptoMarket
from flask_socketio import SocketIO
import threading
import websockets
import asyncio

async def handler(websocket, path):
 
    data = await websocket.recv()
 
    reply = f"Data recieved as:  {data}!"
 
    await websocket.send(reply)


app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
app.secret_key = 'DESIGN/IS/MY/PASSION'
CORS(app)
Session(app)
app.register_blueprint(user_service, url_prefix='/users')
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def main():
    return "Hello there"

@socketio.on('connect')
def test_connect():
    print('someone connected to websocket')

if __name__ == "__main__":
    thread_crypto_market = threading.Thread(target=get_crypto_market_data)
    thread_crypto_market.start()
    start_server = websockets.serve(handler, "localhost", 8000)
    asyncio.get_event_loop().run_until_complete(start_server)
    
    asyncio.get_event_loop().run_forever()
    SocketIO.run(app)
    thread_crypto_market.join()




