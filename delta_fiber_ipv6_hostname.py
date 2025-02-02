import ipaddress

prefix = int( ipaddress.IPv6Address( '2001:4c3c:4900::' ) ) # Delta Fiber Nederland

charset = 'ojelwtfn40ryg5z7dbs9mahqv16kc3ipx8u2'
out = ''

def encode( ip ):
    ip = int( ipaddress.IPv6Address( ip ) ) & 0xFFFFFFFFFFFFFFFFFFFFFF
    out = ''
    while ip:
        c = ip % 36
        out += charset[c]
        # must use integer division as floats get truncated
        ip = ip // 36
    return out

def decode( estring ):
    ip = 0
    for c in reversed(estring):
        ip *= 36
        ip += charset.index(c)
    return ipaddress.IPv6Address(ip + prefix) 

ipv6address = '2001:4c3c:4915:7200:3f1e::2222'
print("ipv6address:", ipv6address)
enc = encode(ipv6address )
print( 'Encoded:', enc )
decoded = decode( enc )
print( 'Decoded:', decoded )
