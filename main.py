from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "people_data"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"{(self.ssn)} {self.firstname} {self.lastname} ({self.gender},{self.age})"


class Thing(Base):
    __tablename__ = "Things"
    tid = Column("tid", Integer, primary_key=True)
    des = Column("Des", String)
    owner = Column("owner", Integer, ForeignKey("people_data.ssn"))

    def __init__(self, tid, des, owner):
        self.tid = tid
        self.des = des
        self.owner = owner

    def __repr__(self):
        return f"{(self.tid)}{self.des} owned by {self.owner}"



engine = create_engine("sqlite:///mydb.db")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

p1 = Person(123, "mike","lara","m",34)
p2 = Person(124, "m","lra","m",34)
p3 = Person(125, "mi","lra","m",34)
p4 = Person(143, "mie","lr","m",34)
p5 = Person(543, "mik","lar","m",34)

session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)
session.add(p5)


t1 = Thing(1,"car", p1.ssn)
t4 = Thing(4,"car1",p2.ssn)
t3 = Thing(3,"ca", p3.ssn)
t7 = Thing(7,"ca3", p2.ssn)
t2 = Thing(2,"ca4", p5.ssn)


session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)
session.add(t7)

session.commit()

