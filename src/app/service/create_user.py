def create_user(name, age):
    session = Session()
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    session.close()