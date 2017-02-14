
from channels.routing import route
from myapp.consumers import ws_message

# channel_routing = [
#     route("http.request", "myapp.consumers.http_consumer"),
# ]
channel_routing = [
    route("websocket.receive", ws_message),
]
