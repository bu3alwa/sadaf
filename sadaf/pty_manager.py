import os
import pty
import tty
import termios

def create_pty():
    master, slave = pty.openpty()
    return (master, slave)

if __name__ == '__main__':
    pass
