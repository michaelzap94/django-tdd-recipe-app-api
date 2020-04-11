# #import patch function from unittest.mock
# #This will help us MOCK behaviour of Django get_database function
# #Simulate the DB being available or NOT
# from unittest.mock import patch

# #
# from django.core.management import call_command
# #OperationalError that django throws when DB is NOT available
# from django.db.utils import OperationalError
# #Import TestCase
# from django.test import TestCase

# class CommandTests(TestCase):
#     def test_wait_for_db_ready(self):
#         pass