-- FastAPI API testing for the Asyncronize

- Install the requirements
```
>> python311 -m pip install -r requirements.txt
```

- Run the application of the Python311
```
>> python311 -m uvicorn app:app --reload
```

- Run the application of the App Task
```
>> python311 -m uvicorn apptask:app --host 127.0.0.1 --port 8015 --reload 
```

```
ulimit -n 4096

```