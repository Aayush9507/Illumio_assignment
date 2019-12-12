import csv
from collections import OrderedDict
from Rule import Rule
from Ip_Range import Range


class Firewall(object):

    csv_path = None
    rule_map = OrderedDict()

    def __init__(self, csv_path):
        """This constructor populates the rules from csv file into a sorted Hashmap"""

        self.csv_path = csv_path
        self.rule_map = OrderedDict()

        with open(csv_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.insert_rule(row)

    def accept_packet(self, direction, protocol, port, ip_address):
        return self.is_allowed(direction, protocol, port, ip_address)

    def is_allowed(self, direction, protocol, port, ip_address):
        """This function checks whether the input packet should be allowed by Firewall according to
        the rules in Hashmap"""

        if port not in self.rule_map:
            return False
        else:
            rule_entry = self.rule_map[port]
            allowed_ip = rule_entry.iprange
            return rule_entry.is_allowed(direction, protocol) and allowed_ip.includes(ip_address)

    def insert_rule(self, row):
        """This function inserts new rule into rule map and if a rule already exists then updates the
        existing rule"""
        IP = Range(row[3])

        if '-' in row[2]:
            # Port is ranged
            port_range = row[2].split("-")
            start = int(port_range[0])
            end = int(port_range[1])

            for port in range(start, end + 1):
                if int(port) in self.rule_map:
                    existing_rule = self.rule_map[int(port)]
                    existing_rule.extend_permission(Rule(row[0], row[1], IP))

                self.rule_map[int(port)] = Rule(row[0], row[1], IP)
        else:
            # Port is fixed
            port = row[2]
            if int(port) in self.rule_map:
                existing_rule = self.rule_map[int(port)]
                existing_rule.extend_permission(Rule(row[0], row[1], IP))

            self.rule_map[int(port)] = Rule(row[0], row[1], IP)