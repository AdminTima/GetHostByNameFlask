import socket
from flask import Flask, render_template, request

app = Flask(__name__)


def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return 'Invalid hostname'


res = get_ip('yandex.ru')
print(res)


@app.route('/', methods=['POST', 'GET'])
def index():
    error = ''
    adress = ''
    hostname = ''
    if request.method == 'POST':
        hostname = request.form['hostname']
        if hostname:
            adress = get_ip(hostname)
        else:
            error = 'You did not type anything'
    return render_template('index.html', adress=adress, hostname=hostname)
