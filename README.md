#Firewall

Assignment for Illumio

###Firewall Class
- ```__init__```: Constructor - Reads csv from input file path and populates the Hashmap
of rules.
- ```accept_packet```: Function - Checks if a packet should be allowed by firewall or not.
- ```insert_rule```: Function - Inserts new rule from CSV file, if a rule already exists then updates the rule.

###Idea and Approach
- I used a hashmap to store ports as key and a Rule object as value. The Rule object has allowed IP range object, allowed protocol and allowed direction as its properties.

- To insert a new rule, I simply made PORT as key and a Rule object as value.
If a rule already exists then I simply update the rule. Ex- If IP range needs to be extended or inbound or outbound direction needs to be changed.

- To check if a packet should be allowed, the program find the PORT in ```rule_map``` (hashmap of rules).
If the port doesn't exist in ```rule_map``` then packet is discarded. Whereas if the PORT exists
it simply gets its Rule object and compares if the direction, protocol and IP range matches.

###Improvements
- Although this hashmap allows constant access time the reads are very fast, while adding new rules if the port is a range then my function iterates through the port range and adds new key value pairs which is memory inefficient and allows duplicacy.
If I had more time then I would have tried to implement a Trie data structure with IP addresses.
 
- I think this approach is read efficient but write heavy.
Assuming there would be more reads(accepting packets) than writes(adding new rules) I chose to take ports as KEY.
If the port range is long then a lot of memory would be wasted.

###Testing
I created a script to generate upto 500,000 lines of CSV.
Due to less time, I could only test this program with the example input provided in pdf.
To run tests simply run ```Test.py```

###Team
My first preference would be Platform team and second preference as Data team or Policy team.

###Message to Reviewer
Thank you for taking the time to review my code.
I would like to mention that apart from strong foundation in data structures, algorithms and OOPS,
I have excellent R&D and Troubleshooting skills as well.