# orbital
Tech test for Orbital Witness

## Setup

1. Clone the repo
1. Make sure you have poetry installed (https://python-poetry.org/docs/#installation) and it is on your path
1. Run `poetry install` to install dependencies
1. Run `poetry run uvicorn src:app --reload` to start the server
1. To run tests, run `poetry run pytest`

## Rubric

- I want to build a rest API using FastAPI
- I will try not to use a database because this is a read only app and it will save time
- Order of tasks:
    - Handle list endpoint
    - Handle pagination
    - Handle detail endpoint
    - Handle ordering by ID
    - Handle desc and asc ordering
    - Handle ordering by title_number
    - Handle filtering by title_class

- I will try to use libraries to do the heavy lifting, because this would be a lot of work to do from scratch
