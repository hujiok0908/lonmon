import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "248e5598-e806-4604-b52b-55b23eb81bc4")
    .replace("__vl__", "/vless")
    .replace("__vm__", "/vmess")
    .replace("__tr__", "/tr")
)