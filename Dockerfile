FROM alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apk add python3

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . . 


#CMD ["python","./backout.py"]
