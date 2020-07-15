import flask
from flask import Flask, send_from_directory, render_template, request, redirect, url_for, send_file
import telethon
from telethon.sync import TelegramClient, events
import asyncio

loop = asyncio.get_event_loop()
app = Flask(__name__)
import asyncio



user = TelegramClient("m4", 949749, "b67eba7db41cbe3799d551f451f54acb", device_model="Xiaomi Redmi Note 4",
                      system_version="5.10.0", app_version="10 P (27)")
user.start()


async def send_users(link):
    users=await user.get_participants(link)
    list_data=[]
    for i in users:
            if i.username!=None:
             list_data.append(i.username)
    print(len(users))
    f=open("static\\file.txt",mode="w")
    for i in list_data:
        f.write(str(i)+"\n")
    f.close()

@app.route('/parser',methods=['GET',"POST"])
def hello_world():
    list=[]

    if request.method == 'POST':
        link = request.form['link']
        loop.run_until_complete(send_users(link))
        return app.send_static_file('file.txt')

    else:
     return render_template("parser.html")

@app.route("/")
def main():
    return render_template("index.html")



if __name__ == '__main__':
    app.run()
