#pip install speedtest-cli
from speedtest import Speedtest

sp = Speedtest()
print("Your connection's Download speed is",sp.download())
print("Your connection's upload speed is", sp.upload())
