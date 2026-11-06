FROM python:3.13
ENV DATABASE_NAME="book_store"
ENV DATABASE_HOST="postgres:password@book_store_db"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]



# This does 4 things
# 1 - Starts with a base python environment
# 2 - Copies your app file into the container
# 3 - Installs dependencies
# 4 - Defines the command to run the app


