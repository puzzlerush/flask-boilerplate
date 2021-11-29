# flask-boilerplate

## Build server image
`docker-compose build`

## Run the container
`docker-compose up`

## Create the db for the first time
`docker-compose exec server sh`  
`flask db migrate -m "Initial migration"`  
`flask db upgrade`
