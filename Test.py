from Firewall import Firewall
import unittest


firewall_obj = Firewall("/Users/mymac/PycharmProjects/illumio_coding_challenge/test.csv")


class TestStringMethods(unittest.TestCase):

    def test_input(self):
        # Assuming input will be a valid entry
        self.assertTrue(firewall_obj.is_allowed("inbound", "tcp", 80, "192.168.1.2"))
        self.assertTrue(firewall_obj.is_allowed("inbound", "udp", 53, "192.168.2.1"))
        self.assertTrue(firewall_obj.is_allowed("outbound", "tcp", 10234, "192.168.10.11"))
        self.assertFalse(firewall_obj.is_allowed("inbound", "tcp", 81, "192.168.1.2"))
        self.assertFalse(firewall_obj.is_allowed("inbound", "udp", 24, "52.12.48.92"))


if __name__ == '__main__':
    unittest.main()