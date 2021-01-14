"""Ping MC Server to see if its running"""

import socket


def ping_server(ip, port):
    """
    Pings a server to see if its running
    :param str ip: Host names IP
    :param int port: Port to connect to Host
    :return: Returns the connection, or if connection is refused, False
    """
    try:
        socket.create_connection((ip, port), 5)
        return True
    except TimeoutError:
        return False
    except socket.timeout:
        return False
