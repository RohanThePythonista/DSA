import binascii

key_hex = "603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4"
key_str = binascii.a2b_hex(key_hex)
print(key_str)
key = list(key_str)
# key2 = [chr(each_key) for each_key in key_str]
print(key)
# print(key2)
# print(binascii.a2b_hex('48656c6c6f20576f726c6421'))
# key: ['`', '=', '\xeb', '\x10', '\x15', '\xca', 'q', '\xbe', '+', 's', '\xae', '\xf0', '\x85', '}', 'w', '\x81', '\x1f',
#       '5', ',', '\x07', ';', 'a', '\x08', '\xd7', '-', '\x98', '\x10', '\xa3', '\t', '\x14', '\xdf', '\xf4']
l = len('66890082dac81b92b873a6dfe8a3a28d')
l2 = len('02250523ff2b0000100000358a0000162020202020202020202020202020202020')
print(l, l2)