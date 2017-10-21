from flask import Flask, request
from user_agents import parse
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    
    # grabbing user agent
    ua_string = request.headers.get('User-Agent')
    user_agent = parse(ua_string)
    is_mobile = user_agent.is_mobile
    is_tablet = user_agent.is_tablet
    is_touch_capable = user_agent.is_touch_capable
    is_pc = user_agent.is_pc
    is_bot = user_agent.is_bot
    string_user_agent = str(user_agent)

    html = "<h3>Hello! {name}!</h3>" \
           "<b>Docker Container Hash:</b> {hostname}<br/>" \
           "<br><br>" \
           "<b>User Agent:</b> {ua}<br>" \
           "<b>Is mobile?</b> {is_mobile}<br>" \
           "<b>Is tablet?</b> {is_tablet}<br>" \
           "<b>Is touch capable ?</b> {is_touch_capable}<br>" \
           "<b>Is PC?</b> {is_pc}<br>" \
           "<b>Is bot? :D</b> {is_bot}<br>" \
           "<b>Your device is:</b> {string_user_agent}"
    return html.format(name="This message are from docker container!", hostname=socket.gethostname(), ua=request.headers.get('User-Agent'), is_mobile=is_mobile, is_tablet = is_tablet, is_touch_capable = is_touch_capable, is_pc = is_pc, is_bot = is_bot, string_user_agent = string_user_agent)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


