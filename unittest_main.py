import unittest
from main import server_status

class TestServerStatus(unittest.TestCase):
    def test_server_status_online(self):
        url = "https://www.motocicletekawasaki.ro/"
        self.assertTrue(server_status(url))

    def test_server_status_offline(self):
        url = "https://gergre.ro/"
        self.assertFalse(server_status(url))


if __name__ == '__main__':
    unittest.main()