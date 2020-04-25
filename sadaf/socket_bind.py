import socket
import threading
import queue
import sys
import tty
import termios

def listener_stdout(conn, thread_stop):
    while not thread_stop:
        try:
            out = conn.recv(1024)
        except socket.timeout:
            pass
        else:
            if out:
                sys.stdout.write(str(out, 'utf-8'))
                sys.stdout.flush()

def listener_stdin(conn):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    tty.setraw(fd)
    new_settings = termios.tcgetattr(fd)
    new_settings[3] = new_settings[3] & ~(termios.ECHO)
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_settings)

    while True:
        user_input = sys.stdin.read(1)

        if user_input == '\x04':
            print("exiting")
            termios.tcsetattr(fd, termios.TCSAFLUSH, old_settings)
            break
        elif user_input:
            try:
                conn.sendall('{}'.format(user_input).encode('utf-8'))
            except Exception as e:
                print(e)

def bind_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((socket.gethostname(), port))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            thread_stop = False
            lis_thread = threading.Thread(target=listener_stdout, args=(conn, thread_stop,))
            lis_thread.setDaemon(True)
            lis_thread.start()

            listener_stdin(conn)

            s.close()
            thread_stop = True
            sys.exit()


if __name__ == "__main__":
    bind_port(443)
