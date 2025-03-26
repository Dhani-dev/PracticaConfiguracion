FROM python:latest

WORKDIR /app
COPY main.py /app/
RUN pip install flask  # Instala Flask dentro del contenedor

CMD ["python", "main.py"]
EXPOSE 80  
