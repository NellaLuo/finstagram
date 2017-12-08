# -*- encoding=UTF-8 -*-

from finstagram import app,db
from flask_script import Manager
from finstagram.models import User,Image,Comment
import random

manager=Manager(app)

def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'

@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0, 100):
        db.session.add(User('User' + str(i), 'a' + str(i)))
        for j in range(0, 3):  # 每人发三张图
            db.session.add(Image(get_image_url(), i + 1))
            for k in range(0, 3):
                db.session.add(Comment('This is a comment' + str(k), 1 + 3 * i + j, i + 1))

    db.session.commit()

    for i in range(50,100,2):
        user=User.query.get(i)
        user.username='[New]'+user.username
    User.query.filter_by(id=51).update({'username':'[New2]'})
    db.session.commit()

    for i in range(50,100,2):
        comment=Comment.query.get(i+1)
        db.session.delete(comment)
    db.session.commit()


    print 1, User.query.all()
    print 2, User.query.get(3)  # primary key = 3
    print 3, User.query.filter_by(id=2).first()
    print 4, User.query.order_by(User.id.desc()).offset(1).limit(2).all()
    print 5, User.query.paginate(page=1, per_page=10).items
    u = User.query.get(1)
    print 6, u
    print 7, u.images
    print 8, Image.query.get(1).user
    # print 7, User.query.get(1).images.filter_by(id=1).first() # Base query:User.query.get(1).images
    # print User.query.filter_by(id=2).first_or_404()

if __name__ == '__main__':
    manager.run()

