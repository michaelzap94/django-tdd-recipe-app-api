#import patch function from unittest.mock
#This will help us MOCK behaviour of Django get_database function
#Simulate the DB being available or NOT
from unittest.mock import patch
from django.core.management import call_command
#OperationalError that django throws when DB is NOT available
from django.db.utils import OperationalError
#Import TestCase
from django.test import TestCase

class CommandTests(TestCase):
    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        # django.db.utils.ConnectionHandler.__getitem__ -> is the function that gets executed when initializing the db
        # therefore, we'll have to make sure that whenever calling it, we do something else(mocking)
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            #mock behaviour of function
            gi.return_value = True
            call_command('wait_for_db') #call our wait_for_db function
            #check __getitem__ was only called once
            self.assertEqual(gi.call_count, 1)

    # check that the wait_for_db tried the db 5 times, and connected on the 6th time
    # mock 'time.sleep' -> replaces behaviour of time.sleep and replaces the return value with None in ts,
    # this is because we don't want the 'time.sleep' behaviour in the 'wait_for_db' function to be holding up/delaying our testing.
    @patch('time.sleep', return_value=None) 
    def test_wait_for_db(self, ts):
        """Test waiting for db"""

        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # side effect -> [oe, oe, oe, oe, oe, True]
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db') #-> this will call 'time.sleep'
            self.assertEqual(gi.call_count, 6)