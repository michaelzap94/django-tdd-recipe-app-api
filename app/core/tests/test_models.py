# # Test that our helper function from our model can create an user
# from django.test import TestCase
# # Gets the default AUTH_USER_MODEL
# # For this project, I made my own in .core/models.py -> User
# from django.contrib.auth import get_user_model


# class ModelTests(TestCase):

#     def test_create_user_with_email_successful(self):
#         """Test creating a new user with an email is successful"""
#         email = 'test@gmail.com'
#         password = 'testpwd'
#         user = get_user_model().objects.create_user(
#             email=email,
#             password=password
#         )

#         self.assertEqual(user.email, email)
#         # You cannot check the password equality because it's encrypted,
#         # but you can check if the password is correct for this user.
#         self.assertTrue(user.check_password(password))

#     def test_new_user_email_normalized(self):
#         """Test the user email is normalized(@secondPart.com is case insensitive)"""
#         email = 'test@GMAIL.COM'
#         user = get_user_model().objects.create_user(email, 'testpwd')

#         self.assertEqual(user.email, email.lower())

#     def test_new_user_invalid_email(self):
#         """Test creating user with no email raises error"""
#         # we want to MAKE SURE everything we run inside raises the 'specified' error
#         with self.assertRaises(ValueError):
#             get_user_model().objects.create_user(None, 'testpwd')

#     def test_create_new_superuser(self):
#         """Test creating a new superuser"""
#         user = get_user_model().objects.create_superuser(
#             'test@super.com',
#             'admin'
#         )

#         self.assertTrue(user.is_superuser)  # is_superuser - This is included in the built-in PermissionsMixin package.
#         self.assertTrue(user.is_staff)  # is_staff - we have it in our OWN custom User Model
