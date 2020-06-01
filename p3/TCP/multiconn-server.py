#!/usr/bin/env python3
#
import sys
import socket
import selectors
import types
#
sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    #print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print(repr(data))
       # conn.send(data)  # Hope it won't block
    else:
       # print('closing', conn)
        sel.unregister(conn)
        conn.close()


with socket.socket() as sock:
    sock.bind(('127.0.0.1', 8080))
    sock.listen(7)
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)

    while True:
        print("Esperando evento...")
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)