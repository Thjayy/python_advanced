def ips_between(start, end):
    start_parts = list(map(int, start.split('.')))
    end_parts = list(map(int, end.split('.')))
    
    num_addresses = 0
    for i in range(4):
        num_addresses += (end_parts[i] - start_parts[i]) * (256 ** (3 - i))
    
    return num_addresses


print(ips_between("10.0.0.0", "10.0.0.50"))
print(ips_between("10.0.0.0", "10.0.1.0"))
print(ips_between("20.0.0.10", "20.0.1.0"))