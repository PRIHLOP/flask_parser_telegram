# import flask
# import sys
# from flask
from flask import Flask, send_from_directory, render_template, request
from telethon.sync import TelegramClient
import asyncio
# from contextlib import redirect_stdout

loop = asyncio.get_event_loop()
app = Flask(__name__)

user = TelegramClient("user", "1989568", "747f20657437007b833f335f7422a156",
                      device_model="Xiaomi Redmi Note 4",
                      system_version="5.10.0", app_version="10 P (27)")
user.start()


async def send_users(link):
    filename = link.split("/")[-1]
    f = open('static//{}.csv'.format(filename), mode="w")
    f.write("User ID;First Name;Last Name;Username;Phone"+"\n")
    count = 0
    async for u in user.iter_participants(link, aggressive=False):
        string = f"{u.id};{u.first_name};{u.last_name};@{u.username};{u.phone}"
#        print(string)
        f.write("%s\n" % string)
        count += 1
    f.close()


@app.route('/parser', methods=['GET', "POST"])
def hello_world():
    if request.method == 'POST':
        link = request.form['link']
        loop.run_until_complete(send_users(link))
        filename = link.split("/")[-1]
        return send_from_directory(directory='static',
                                   filename='{}.csv'.format(filename),
                                   as_attachment=True)
    else:
        return render_template("parser.html")


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
