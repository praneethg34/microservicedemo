from python:slim
USER root
COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
COPY src /src
RUN useradd -ms /bin/sh python
RUN chown -R python:python /src
USER python
WORKDIR /src
ENTRYPOINT [ "python3","main.py" ]