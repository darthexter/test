FROM python:3
ADD calculator.py /
CMD [ "python", "./my_script.py" ]
