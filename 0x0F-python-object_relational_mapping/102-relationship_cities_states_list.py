#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and bind the sessionmaker
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Retrieve all City objects with their associated State objects
    cities = session.query(City).order_by(City.id).all()

    # Print the City objects with corresponding State names
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()

