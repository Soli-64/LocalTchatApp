# coding:utf-8
import socket
import sys
import threading
import tkinter


class ThreadForClient(threading.Thread):
    def __init__(self, conn, func):
        threading.Thread.__init__(self)
        self.conn = conn
        self.func = func

    def run(self):
        while True:
            data = self.conn.recv(1024)
            data = data.decode("utf8")
            self.func(data)
            self.conn.sendall(data.encode('utf8'))


class App:

    def __init__(self, user_name):
        self.user_name = user_name

        self.host, self.port = (str(socket.gethostbyname(socket.gethostname())), 5566)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_host = False

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.window = tkinter.Tk()
        self.window.title(f'Tchat - {self.user_name}')

        self.button_new_session = tkinter.Button(self.window, text='Lancer une nouvelle session',
                                                 command=lambda: threading.Thread(target=self.launch_session).start())
        self.join_button = tkinter.Button(self.window, text="Rejoindre une session", command=self.join_session)

        self.tchat = tkinter.Text(self.window, height=10, width=50)
        self.tchat.config(state=tkinter.DISABLED)

        self.entry = tkinter.Entry(self.window)
        self.send_button = tkinter.Button(self.window, text="Envoyer", command=lambda: print('send_button'))

    """
         Server Part

         -> create_server  : create a server
         -> launch_session : launch server loop and server host join

    """

    def create_server(self):

        self.is_host = True

        self.server.bind((self.host, self.port))
        print(f'Serveur lancé avec succès sur l"ip: {self.host} !')

        while True:
            self.server.listen()
            self.conn, adress = self.server.accept()
            print('Client has just been connected')

            th = ThreadForClient(self.conn, self.add_tchat_message)
            th.start()

        self.conn.close()
        server.close()
        self.client_socket.close()

    def launch_session(self):

        server_loop = threading.Thread(target=self.create_server)
        server_loop.start()

        self.join_session()

    """

        Client Part

        -> join_session

    """

    def pack(self):
        self.button_new_session.pack()
        self.join_button.pack()
        self.tchat.pack(padx=10, pady=10)
        self.entry.pack()
        self.send_button.pack()

    def execute(self):
        self.pack()
        self.window.mainloop()

    def send_server_message(self, message):
        if len(message.strip()) > 0:
            self.client_socket.sendall(f' {self.user_name}: {message}'.encode("utf8"))
            if self.is_host:
                self.conn.sendall(f" {self.user_name}: {message}".encode('utf8'))

    def add_tchat_message(self, message):
        self.tchat.config(state=tkinter.NORMAL)
        self.tchat.insert(tkinter.END, message + '\n')
        self.tchat.config(state=tkinter.DISABLED)

    def waitfor_client_message(self, socket):
        while True:
            data = socket.recv(1024).decode('utf8')
            print(data)
            self.add_tchat_message(data)

    def join_session(self):
        try:

            if self.is_host:
                ip = self.host
            else:
                ip = input('Entrez l"ip souhaité pour vous y connecter -> ')

            self.client_socket.connect((ip, self.port))

            print('Connexion réussie')

            self.send_button.config(command=lambda: self.send_server_message(self.entry.get()))

            if not self.is_host:
                th = threading.Thread(target=self.waitfor_client_message, args=[self.client_socket])
                th.start()

        except ConnectionRefusedError:
            print('Connexion échouée')


if __name__ == '__main__':
    name = input('Entrez votre nom ->')

    app = App(name)
    app.execute()

    data = input('fin du code ?')

    app.server.close()
    app.client_socket.close()

    sys.exit(0)
