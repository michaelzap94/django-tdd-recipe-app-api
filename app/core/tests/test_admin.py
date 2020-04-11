# from django.test import TestCase
# # Gets the default AUTH_USER_MODEL
# # For this project, I made my own in .core/models.py -> User
# from django.contrib.auth import get_user_model
# # Helper function that allows us to generate urls for django page
# from django.urls import reverse
# # Test client that allows us to make "test requests" to our application in our unit test
# from django.test import Client


# class AdminSiteTests(TestCase):

#     # Any initialization I want. It runs before anything else.
#     def setUp(self):
#         # Test client that allows us to test requests to our application in our unit test
#         self.client = Client()

#         # Create a superuser
#         self.admin_user = get_user_model().objects.create_superuser(
#             email='admin@londonappdev.com',
#             password='password123'
#         )
#         # Uses the client HELPER to force the user to LOGIN for us.
#         self.client.force_login(self.admin_user)

#         # Create one NORMAL user, not authenticated
#         self.user = get_user_model().objects.create_user(
#             email='test@londonappdev.com',
#             password='password123',
#             name='Test User Full Name',
#         )

#     def test_users_listed(self):
#         """Test that users are listed on the user page"""
#         # get url:
#         # These urls are defined in the django documentation
#         # APP_THAT_YOU_ARE_GOING_FOR:URL_THAT_YOU_WANT
#         url = reverse('admin:core_user_changelist')  # reverse will generate the URL for OUR list user page.
#         # use test client to perform an HTTP get request
#         res = self.client.get(url)

#         # assertContains -> CHECKS that our 'res' contains a certain item
#         # it also checks for http response to be 200
#         self.assertContains(res, self.user.name)
#         self.assertContains(res, self.user.email)

#     def test_user_change_page(self):
#         """Test that the user edit page works"""
#         # get url:
#         # These urls are defined in the django documentation
#         # APP_THAT_YOU_ARE_GOING_FOR:URL_THAT_YOU_WANT
#         # We need to give an argument containing the user.id
#         url = reverse('admin:core_user_change', args=[self.user.id])
#         # it will be like this ---> /admin/core/user/[ANY ID OF THE USER e.g: 2]

#         res = self.client.get(url)

#         # We check the status_code of the res is 200 so it means we got the result
#         self.assertEqual(res.status_code, 200)

#     def test_create_user_page(self):
#         """Test that the create user page works"""
#         # get url:
#         # These urls are defined in the django documentation
#         # APP_THAT_YOU_ARE_GOING_FOR:URL_THAT_YOU_WANT
#         # We need to give an argument containing the user.id
#         url = reverse('admin:core_user_add')
#         # it will be like this ---> /admin/core/user/[ANY ID OF THE USER e.g: 2]

#         res = self.client.get(url)

#         # We check the status_code of the res is 200 so it means we got the result
#         self.assertEqual(res.status_code, 200)
