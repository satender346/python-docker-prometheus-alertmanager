from prometheus_client import Counter
import requests

apps_metrics = Counter('apps_alerts', 'apps_alerts', ['app_server_name', 'alert', 'description'])

def set_alert_status(server_name, alert_message, description):
    apps_metrics.labels(server_name, alert_message, description).inc()


def check_services():
    server = "http://example.com"
    status = requests.get(server, timeout=10)
    if status.status_code != 200:
       print (f"{server} is Down")
       alert_message = f"Critical- {server} is down"
       alert_description = f"{server} status is not 200"
       set_alert_status(server, alert_message, alert_description)
