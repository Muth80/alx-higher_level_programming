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

    # Create State "California"
    california = State(name="California")

    # Create City "San Francisco"
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    # Add State and City to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the session to the database
    session.commit()

    # Close the session
    session.close()

