FROM python:3-slim
WORKDIR /usr/src/app
COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt
COPY ./signupList.py ./
CMD [ "python", "./signupList.py" ]