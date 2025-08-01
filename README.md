## Helper to run DD agent + DD lambda wrapper
make sure to add your DD_API_KEY in the `.env`

run docker-compose, it should start both the DD agent and the wrapper
```shell
docker-compose up
```

from here we can send a curl request, example from the [documentation usage](https://gallery.ecr.aws/lambda/python)
```curl
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"TEST FROM LOCAL - LOOK FOR THIS MESSAGE!"}
```

this should log `Processing event: {'payload': 'TEST FROM LOCAL - LOOK FOR THIS MESSAGE!'}` in your DD