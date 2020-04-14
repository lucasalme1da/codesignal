def findEmailDomain(address):
   return ''.join(list(address)[len(list(address)) - list(address)[::-1].index('@'):])