"""Ping MC Server to see if its running"""

import socket


class Connection:
    """
    Class that connects to mc server
    """

    def __init__(self, is_connected=False):
        self.is_connected = is_connected

    def ping_server(self, ip, port):
        """
        Pings a server to see if its running
        :param str ip: Host names IP
        :param int port: Port to connect to Host
        :return: Returns the connection, or if connection is refused, False
        """

        try:
            socket.create_connection((ip, port))
            self.is_connected = True
        except TimeoutError:
            self.is_connected = False
