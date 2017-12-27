from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup1 import Category, Base, CategoryMenu

engine = create_engine('sqlite:///catalogmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Guitars Menu
category1 = Category(name="Guitars")

session.add(category1)
session.commit()


categoryMenu1 = CategoryMenu(name="Acoustic Guitars", description="Guitars Description",
                             category=category1)

session.add(categoryMenu1)
session.commit()


categoryMenu2 = CategoryMenu(name="Electric Guitars", description="Electric Guitars Description",
                             category=category1)

session.add(categoryMenu2)
session.commit()

categoryMenu3 = CategoryMenu(name="Acoustic-Electric Guitars", description="Acoustic-Electric Guitars Description",
                             category=category1)

session.add(categoryMenu3)
session.commit()

#Keyboards Menu
category1 = Category(name="Keyboards")

session.add(category1)
session.commit()


categoryMenu1 = CategoryMenu(name="Digital Pianos", description="Digital Pianos Description",
                             category=category1)

session.add(categoryMenu1)
session.commit()

categoryMenu2 = CategoryMenu(name="Arranger Work Stations", description="Arranger Work Stations Description",
                             category=category1)

session.add(categoryMenu2)
session.commit()

#Violins Menu
category1 = Category(name="Violins")

session.add(category1)
session.commit()


categoryMenu1 = CategoryMenu(name="Electric Violins", description="Electric Violins Description",
                             category=category1)

session.add(categoryMenu1)
session.commit()



print "added menu items!"
