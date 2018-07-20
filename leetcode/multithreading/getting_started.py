import threading


def hello_world(name):
    print('Hello World {} !!'.format(name))


name = 'Soumasish'

t = threading.Thread(target=hello_world, args=(name,))
t.start()
t.join()
