
"""
This class represents a rule for each IP/Port combination
"""


class Rule:
    is_Inbound = False
    is_Outbound = False
    is_Tcp = False
    is_Udp = False
    iprange = None

    def __init__(self, direction, protocol, iprange):
        if direction == "outbound":
            self.is_Outbound = True
        else:
            self.is_Inbound = True

        if protocol == "tcp":
            self.is_Tcp = True
        else:
            self.is_Udp = True

        self.iprange = iprange

    def is_allowed(self, direction, protocol):
        if direction == "outbound":
            allowed_dir = self.is_Outbound
        else:
            allowed_dir = self.is_Inbound

        if protocol == "tcp":
            allowed_protocol = self.is_Tcp
        else:
            allowed_protocol = self.is_Udp

        return allowed_dir and allowed_protocol

    def extend_permission(self, new_rule):
        """If a rule already exists then extend its permission, we should not override"""

        if new_rule.is_Inbound:
            self.is_Inbound = True
        if new_rule.is_Outbound:
            self.is_Outbound = True
        if new_rule.is_Tcp:
            self.is_Tcp = True
        if new_rule.is_Udp:
            self.is_Udp = True

        self.iprange = new_rule.iprange