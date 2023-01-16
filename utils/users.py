from django.contrib.auth.models import User


def create_non_staff(username, email, password, first_name, last_name):
    """
    Create a new user and save it to the database.
    """
    # Create user and save to the database
    user = User.objects.create_user(username, email, password)

    # Update fields and then save again
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    return user

def create_knot_an_admin():
    """
    Create a specific user, `KnotAnAdmin`, and save it to the database.
    """
    # Create user and save to the database
    user = User.objects.create_user('KnotAnAdmin', 'KnotAnAdmin@email.app', '1234test')

    # Update fields and then save again
    user.first_name = 'KnotAn'
    user.last_name = 'Admin'
    user.save()
    return user
