FROM python:alpine3.14 AS build-stage
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .

FROM python:alpine3.14
COPY --from=build-stage opt/venv opt/venv
COPY app.py app.py
ENV PATH="/opt/venv/bin:$PATH"
RUN chmod +x app.py
ENTRYPOINT [ "python", "app.py" ]
