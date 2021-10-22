FROM python 

COPY main.py main.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Abrimos el puerto 5000
EXPOSE 5000

CMD ["python","main.py"]