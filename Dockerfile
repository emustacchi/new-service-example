# First stage Creating docker image infrastructure and install dependencies
FROM docker-registry.cyren.io/devops/python:3.7 as Base
WORKDIR /build

# Environment variables
ENV APP_DIR /app
ENV KUBE_LATEST_VERSION=v1.13.3

# Copy app and set workdir
RUN mkdir ${APP_DIR}
COPY requirements.txt ${APP_DIR}
COPY . .

# Install dependencies and cleanup
RUN pip install --no-cache-dir -r requirements.txt

####################################################################################
# Second stage Running the microservice unit tests and integrating to sonarqube

RUN unit_test.sh

ARG build
ARG SONAR_BRANCH_NAME
ARG SONAR_PROJECT_NAME=unknown
ARG SONAR_PROJECT_VERSION=unknown
ARG SONAR_PROJECT_KEY=unknown
ARG SONAR_HOST_URL=undefined

LABEL image=test \
      build=${build}

ENV SONAR_PARAMS="-Dsonar.coverage.exclusions=**/tests/** \
                    -Dsonar.tests=tests \
                    -Dsonar.test.inclusions=**/test_*.py"

RUN sonar.sh ${SONAR_PARAMS}

# Third stage run the app

CMD ["./keepappup.sh"]