from api import app
from api.models.user import UserModel


@app.cli.command('createsuperuser')
def create_superuser():
    """
    Creates a user with the admin role
    """
    username = input("Username[default 'admin']:")
    password = input("Password[default 'admin']:")
    user = UserModel(username, password, role="admin", is_staff=True)
    user.save()
    print(f"Superuser create successful! id={user.id}")
