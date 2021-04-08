from nslookup import Nslookup
import fileinput
import time

#enter a path of Domain List
infile = open('/home/crimson/Downloads/domains.txt', 'r')
filestr = infile.read()
words = filestr.split()

print("Started...")
dns_query = Nslookup(dns_servers=["8.8.8.8"])
print("DNS Server is Set to 8.8.8.8")

print("Querying Domains Please Wait...")
for domain in words:
    ips_record = dns_query.dns_lookup(domain)
    print(ips_record.response_full, ips_record.answer)

    time.sleep(1)
    
    dns_record = dns_query.soa_lookup(domain)
    print(dns_record.response_full, dns_record.answer)

    time.sleep(1)
    #1 second Gap Before querying 