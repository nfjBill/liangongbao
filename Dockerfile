FROM lgb-base:1.1

WORKDIR /
ADD ./ ./

ENV LANG C.UTF-8

ENTRYPOINT ["python", "main.py"]