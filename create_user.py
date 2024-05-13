from app import app

with app.app_context():
    from app.model import Usuario

    user = Usuario(
        username= 'campcode',
        password= '123456',
        admin= True
    )

    user.save()