from sqlmodel import Session, select
from bcrypt import checkpw

from python_web_project_template.functions.hashing import hash_password

from python_web_project_template.database import DATABASE
from python_web_project_template.database.models import User



def test_user():
    """
        Tests user creation.
    """

    with Session(DATABASE) as session:
        session.add(User(username='JohnDoe', email='john@doe.gov', password=hash_password('123456789'))) # never store plaintext passwords!
        session.commit()

        user = session.exec(select(User).where(User.email == 'john@doe.gov')).first()
        assert checkpw(b'123456789', user.password.encode('utf-8'))
        print(user.username, 'OK')

        session.delete(user)
        session.commit()



if __name__ == '__main__':
    test_user()
