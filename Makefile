IMAGE_NAME=iris_flask_app

build:
	docker build -t $(task4) .

# Run the Docker container
run:
	docker run -p 5000:5000 $(task4)


