import unittest
import Event as e

class TestEvent(unittest.TestCase):
    def test_event_creation(self):
        event = e("birthday", "2022-01-01", "John")
        self.assertEqual(event.name, "birthday")
        self.assertEqual(event.date, "2022-01-01")
        self.assertEqual(event.organizer, "John")

if __name__ == '__main__':
    unittest.main()
