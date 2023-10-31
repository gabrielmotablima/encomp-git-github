FROM python:3.8.18-slim

WORKDIR /workspace

COPY . /workspace/

RUN pip install -r /workspace/requirements.txt

EXPOSE 7860

ENTRYPOINT ["python", "/workspace/server.py"]
