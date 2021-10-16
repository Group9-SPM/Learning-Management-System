FROM python:3-slim
WORKDIR /usr/src/app
COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt
COPY ./signuplist.py ./
CMD [ "python", "./signuplist.py" ]