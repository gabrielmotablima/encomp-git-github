FROM python:3.8

ARG GRADIO_SERVER_PORT=7860
ENV GRADIO_SERVER_PORT=${GRADIO_SERVER_PORT}

WORKDIR /workspace

COPY . /workspace/

RUN pip install -r /workspace/requirements.txt

CMD ["python", "/workspace/server.py"]

EXPOSE 7860
