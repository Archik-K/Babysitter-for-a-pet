FROM python:3.10

WORKDIR /flask

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

EXPOSE 443

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install -r requirements.txt

COPY . .

RUN mkdir media

VOLUME ./media