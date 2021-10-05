FROM alpine
RUN apk add python3 && ln -sf python3 /usr/bin/python
ADD calculator.py /
CMD [ "python3", "./calculator.py" ]
