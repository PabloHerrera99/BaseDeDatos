FROM python:3
RUN git clone https://github.com/PabloHerrera99/BaseDeDatos.git
WORKDIR /BaseDeDatos
CMD ["python3", "-m", "my_test"]