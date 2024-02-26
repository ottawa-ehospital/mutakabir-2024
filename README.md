# SYSC5301-data-science-for-biomedical-engineering-project-prod

This repo contains the code for model deployment APIs.
Instructions to deploy the application are given below.


## Deployment Instructions
The two ways of deployment are as follows:

### Docker
```
docker build -t sysc5301-api .
docker run -d --name sysc5301-api -p <host_port>:8080 sysc5301-api
```

### Local 
```
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port <host_port>
```
