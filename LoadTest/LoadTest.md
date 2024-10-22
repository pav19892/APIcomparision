- Locust 

```
Hey GPT 

I am not sure but is locust is able to create the scenario with single thread 

if it is 

then please create script for the load testing script 

Node js script run on  the http://localhost:3000
Flask -> http://localhost:8013
fastapi -> http://localhost:8015
django-drf -> http://localhost:8014
```



Yes, Locust can be used to create load testing scenarios, including single-threaded testing. Locust is a Python-based tool for distributed, scalable, and web application performance testing. You can simulate user behavior by making HTTP requests to your APIs running on different servers (like Node.js, Flask, FastAPI, and Django-DRF).

I'll guide you through creating a single-threaded Locust load test for the APIs running on different ports:

Step-by-Step Guide
1. Install Locust: First, install Locust using pip:

```
python311 -m pip install -r requirements.txt
```

2. Create Locust Script: Create a file named `locustfile.py` and add the following code to simulate load testing on each of your API servers.


- To Run the application

```
python311 -m locust -f locustfile.py
```