import time
from prometheus_client import start_http_server
from . import apps
def main():
    start_http_server(8000) 
    apps.check_services()
    time.sleep(60)
