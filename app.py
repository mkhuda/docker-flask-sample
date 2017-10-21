from flask import Flask, request
from redis import Redis, RedisError
from user_agents import parse
import os
import socket

# Connect to Redis
redis = Redis(host="localhost", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"
    
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
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}" \
           "<br><br>" \
           "<b>User Agent:</b> {ua}" \
           "<b>Is mobile?</b> {is_mobile}" \
           "<b>Is tablet?</b> {is_tablet}" \
           "<b>Is touch capable ?</b> {is_touch_capable}" \
           "<b>Is PC?</b> {is_pc}" \
           "<b>Is bot? :D</b> {is_bot}" \
           "<b>Your device is:</b> {string_user_agent}"
    return html.format(name="This message are from docker container!", hostname=socket.gethostname(), visits=visits, ua=request.headers.get('User-Agent'), is_mobile=is_mobile, is_tablet = is_tablet, is_touch_capable = is_touch_capable, is_pc = is_pc, is_bot = is_bot, string_user_agent = string_user_agent)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


