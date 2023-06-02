# Chess Software

This is a chess software that allows users to manage tournaments and players.

## Installation

### Using pipenv

1.  Clone the repository:

```bash
git clone https://github.com/MickaelFioretti/ChessSoftware.git
```

2.  Create a virtual environment and activate it:

```bash
pipenv --python 3.11
```

```bash
pipenv shell
```

3.  Install the dependencies:

```bash
pip install -r requirements.txt
```

4.  Run the application:

```bash
python app/src/main.py
```

### Using Docker

1.  Clone the repository:

```bash
git clone https://github.com/MickaelFioretti/ChessSoftware.git
```

2.  Build the Docker image:

```bash
docker-compose build
```

3.  Start the Docker container:

```bash
docker-compose up -d
```

4.  Access the Docker container:

```bash
docker exec -it 'container_id' bash
```

5.  Run the application:

```bash
python3 app/src/main.py
```

## Usage

Once the application is running, you can use the main menu to create tournaments and players, and to display reports on the tournaments and players.

To launch the main program, execute the command in the terminal.

```bash
python3 app/src/main.py
```

### Test

For run test you can install 

```bash
install sudo apt install python3-pytest
```

And run this command

```bash
pytest-3
```


## Flake8

For generate a report flake8 you can run this command

```bash
flake8 --format=html --htmldir=flake-report
```