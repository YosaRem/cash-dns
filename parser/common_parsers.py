def domain_to_bytes_str(domain):
    parts = domain.split(".")
    res = ""
    for i in parts:
        res += "{:02x} ".format(len(i)) + " ".join("{:02x}".format(ord(e)) for e in i) + " "
    return res


def str_to_hex(data):
    return bytearray.fromhex(data)

