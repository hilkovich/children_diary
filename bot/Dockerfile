FROM python:3.12

WORKDIR /bot

COPY requirements.txt /bot

RUN pip install --upgrade pip && pip install -r /bot/requirements.txt

VOLUME /children_diary/data_bot

EXPOSE 8080

COPY . /bot

CMD ["python", "app.py"]
