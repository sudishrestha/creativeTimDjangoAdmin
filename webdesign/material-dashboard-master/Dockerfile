FROM python:3.8
LABEL np.com.lionelrg.version=v1.1
ENV PYTHONBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=myproject.settings
ENV PORT 5000
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE $PORT
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
