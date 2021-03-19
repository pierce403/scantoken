# https://web3py.readthedocs.io/en/stable/web3.eth.account.html#prepare-message-for-ecrecover-in-solidity

from web3 import Web3

from web3.auto import w3
from eth_account.messages import encode_defunct

from eth_abi import encode_abi

import binascii

nonce = 1
wei = 1000000000000000000
amount = 500*wei
address = '0x7ab874Eeef0169ADA0d225E9801A3FfFfa26aAC3' # me
#address = '0x1e5A41aBF9A83e1346978414Ae4e001b50b0431f' # token well

msg = encode_abi(['uint256','uint256','address'],[nonce,amount,address])

print("message: "+str(binascii.hexlify(msg)))

# widely known private key, DO NOT USE IN PRODUCTION
private_key = b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d"

message = encode_defunct(msg)
signed_message = w3.eth.account.sign_message(message, private_key=private_key)

print("Encoded Message:")
print(message)

print("Signed Message:")
print(signed_message)

def to_32byte_hex(val):
  return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))

ec_recover_args = (msghash, v, r, s) = (
   Web3.toHex(signed_message.messageHash),
   signed_message.v,
   to_32byte_hex(signed_message.r),
   to_32byte_hex(signed_message.s),
)

print("Message: "+str(binascii.hexlify(msg)))
print("EC Recover Info:")
print(ec_recover_args)

myaddr = w3.eth.account.recover_message(message, signature=signed_message.signature)
print(myaddr)

