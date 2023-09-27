## Installation

```bash
docker build -t service .

or 

make service_docker_run

or 

service_docker_compose 
```

HOW TO TEST: 
```url
http://0.0.0.0:9090/api/v1/weather (get the weather today)


http://0.0.0.0:9090/api/v1/weather/2023-09-27 (token require)

You could send the request in order to test it
GET http://0.0.0.0:9090/api/v1/weather/2023-09-27
x_token: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

```