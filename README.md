# Chess Software

This is a chess software that allows users to manage tournaments and players.

## Installation

### Using venv

1.  Clone the repository:

```bash
git clone https://github.com/MickaelFioretti/ChessSoftware.git
```

2.  Create a virtual environment and activate it:

```bash
python -m venv venv
```

```bash
source venv/bin/activate
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
python app/src/main.py
```

## Usage

Once the application is running, you can use the main menu to create tournaments and players, and to display reports on the tournaments and players.

To launch the main program, execute the command in the terminal.

```bash
python app/src/main.py
```

install sudo apt install python3-pytest
pytest-3
