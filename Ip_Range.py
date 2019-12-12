"""Class for range of IP addresses"""
import ipaddress


class Range:
    start = None
    end = None

    def __init__(self, ip):
        if "-" in ip:
            start, end = ip.split('-')
            self.start = self.ip_to_long(start)
            self.end = self.ip_to_long(end)
        else:
            self.start = self.ip_to_long(ip)
            self.end = self.ip_to_long(ip)

    def ip_to_long(self, ip):
        """Converts IP address to Long integer for easy comparison of IP address range
        using inbuilt python library"""

        return int(ipaddress.IPv4Address(ip))

    def includes(self, ip):
        return self.start <= self.ip_to_long(ip) <= self.end



