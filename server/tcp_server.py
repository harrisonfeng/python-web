#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TCP Server
#
# Copyright (C) 2016 Harrison Feng <feng.harrison@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see [http://www.gnu.org/licenses/].
#
# This is the simpliest tcp server implementation in Python
#
# @author Harrison Feng <feng.harrison@gmail.com>
# @file tcp_server.py


import logging
import socket


logging.basicConfig(level=logging.INFO, 
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOG = logging.getLogger(__name__)


def service(host='', port=12000):
    """Implement a tcp server to accept requests."""

    svr_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    svr_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    svr_sock.bind((host, port))
    svr_sock.listen(1)
    print "The server is ready to receive at {0} now".format(port)
    while True:
        conn, addr = svr_sock.accept()
        request = conn.recv(1024)
        paras = request.strip().split('\n')[0].split(' ')[1].strip('/')
        LOG.info("The request received: {0}".format(request))
        response =  "HTTP/1.1 200 OK\n\nHello, {0}\n".format(paras)
        conn.sendall(response)
        conn.close()


def main():
    service()


if __name__ == "__main__":
    main()
