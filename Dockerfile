FROM python
COPY . .
RUN mkdir -p reports/allure-report
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    xvfb \
    --no-install-recommends
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install \
    && playwright install-deps
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && rm -rf /var/lib/apt/lists/*
CMD ["pytest", "--alluredir=reports/allure-report"]