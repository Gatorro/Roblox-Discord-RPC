from websocket_server import WebsocketServer as wss
from pypresence import Presence
import time
import psutil
import requests
import logging
import re

clients = {}

#=============<>=============#

______THE_APPLICATION_ID______ = ""

#=============<>=============#




rpc = Presence(______THE_APPLICATION_ID______) 
rpc.connect()
timee = int(time.time())

server = wss(host='127.0.0.1', port=8080, loglevel=logging.INFO)
def new_client(client, server):
   clientid = client["id"]
   clients[client["id"]] = client
   print(f"NewClient: {clientid}")

def message_received(client, server, message):
   def add(cmd):
      return re.search(f"^{cmd}",message)
   Args = message.split("|")
   gameName = Args[0]
   gameId = Args[1]
   customFont = {'q': '𝐪', 'w': '𝐰', 'e': '𝐞', 'r': '𝐫', 't': '𝐭', 'y': '𝐲', 'u': '𝐮', 'i': '𝐢', 'o': '𝐨', 'p': '𝐩', 'a': '𝐚', 's': '𝐬', 'd': '𝐝', 'f': '𝐟', 'g': '𝐠', 'h': '𝐡', 'j': '𝐣', 'k': '𝐤', 'l': '𝐥', 'z': '𝐳', 'x': '𝐱', 'c': '𝐜', 'v': '𝐯', 'b': '𝐛', 'n': '𝐧', 'm': '𝐦', 'Q': '𝐐', 'W': '𝐖', 'E': '𝐄', 'R': '𝐑', 'T': '𝐓', 'Y': '𝐘', 'U': '𝐔', 'I': '𝐈', 'O': '𝐎', 'P': '𝐏', 'A': '𝐀', 'S': '𝐒', 'D': '𝐃', 'F': '𝐅', 'G': '𝐆', 'H': '𝐇', 'J': '𝐉', 'K': '𝐊', 'L': '𝐋', 'Z': '𝐙', 'X': '𝐗', 'C': '𝐂', 'V': '𝐕', 'B': '𝐁', 'N': '𝐍', 'M': '𝐌'}
   translation = str.maketrans(customFont)
   gameFont = Args[0].translate(translation)
   url = f"https://www.roblox.com/games/{gameId}/game-name"
   button = [{"label": "Game Link", "url": url}]
   print(gameFont)
   rpc.update(buttons=button,details="𝙋𝙡𝙖𝙮𝙞𝙣𝙜",state=" "+gameFont,start=timee,large_image="roblox512")
def onLeft(client, server):
   rpc.update(details="𝗜𝗱𝗹𝗲",state=" ...",start=timee,large_image="roblox512")
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.set_fn_client_left(onLeft)
server.run_forever()
