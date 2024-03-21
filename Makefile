IMAGE_NAME=iris_flask_app

build:
	docker build -t iris .

# Run the Docker container
run:
	docker run -p 5000:5000 iris


