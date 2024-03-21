FROM python:3.12.2-slim
WORKDIR /app
#COPY . /app

# Install virtualenv
RUN pip install virtualenv

# Create and activate virtual environment
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

CMD ["python3","app.py"]


