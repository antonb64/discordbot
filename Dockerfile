FROM python
RUN mkdir /app
WORKDIR /app
RUN pip install discord
COPY . .
CMD python ./bot.py