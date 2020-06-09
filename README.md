# python-docker-prometheus-alertmanager
End to end automation to monitor application and send critical notification


### Sample python code to monitor an application, export prometheus metric and send alerts using alertmanager in docker environment


### This sample code to check if http://www.example.com is running or not, and send an alert

### Setup

```
git clone https://github.com/satender346/python-docker-prometheus-alertmanager.git

cd python-docker-prometheus-alertmanager/alerting_scripts

vi alertmanager.yml

# update email, stmp server details

cd python-docker-prometheus-alertmanager/

vi docker-compose.yaml

# find and update 'extra_hosts' ips
```

### Deployment

```
cd python-docker-prometheus-alertmanager/

docker build -t monitoring_scripts .

docker-compose up

```

![image](https://user-images.githubusercontent.com/13794845/84206569-0b8e6b80-aa75-11ea-9e29-3d69532b97e4.png)

![image](https://user-images.githubusercontent.com/13794845/84206335-902cba00-aa74-11ea-8209-1d305f0e50e7.png)
