FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Add EXPOSE 5000 to document the listening port
EXPOSE 5000

# Use Gunicorn to run the app reliably in production
# Assumes your app is defined as 'app' in 'app.py'
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]