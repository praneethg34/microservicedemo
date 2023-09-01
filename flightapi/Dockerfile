from python:slim
USER root
COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
COPY src /src
RUN useradd -ms /bin/sh python
RUN chown -R python:python /src
RUN chmod +x /src/entrypoint.sh
USER python
WORKDIR /src
ENTRYPOINT [ "./entrypoint.sh" ]