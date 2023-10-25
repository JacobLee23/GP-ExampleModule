FROM python:3.9.18-slim-bullseye

COPY . .

# Install pipenv for package dependency installation.
RUN python -m pip install pipenv

# Install package dependencies.
#
# Since Docker provides an isolated environment, there is no need to create a virtual environment
# with `$ pipenv shell` within the container, so use --system to install packages to the system
# site-packages instead of to a virtual environment.
#
# Use --deploy to ensure that Pipfile.lock is up-to-date, or abort installation if Pipfile.lock is
# out-of-date.
#
# Use --ignore-pipfile to install packages directly from Pipfile.lock (as opposed to installing
# from Pipfile)
RUN pipenv install --system --deploy --ignore-pipfile

# Configure container to run as an executable
#
# $ docker build -t gpexamplemodule:latest .
# $ docker run gpexamplemodule:latest [-h] [-f FILENAME] [-o OUTPUT] [-v]
ENTRYPOINT ["python", "-m", "gpexamplemodule"]
