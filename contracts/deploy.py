import json
from web3 import Web3
#to connect to ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
address = "<enter your address"
private_key = "<Enter your private key>"


acct = w3.eth.account.privateKeyToAccount(private_key)

# compile your smart contract with truffle first
truffleFile = json.load(open('./build/contracts/ContactList.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']
contract= w3.eth.contract(bytecode=bytecode, abi=abi)
#build transaction
transaction = contract.constructor().buildTransaction(
    {
    "chainId": chain_id,
    "gasPrice": w3.eth.gas_price,
    "from": address,
    "nonce": w3.eth.getTransactionCount(acct.address),
    }
)
# Sign the transaction
sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying Contract!")
# Send the transaction
transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
# Wait for the transaction to be mined, and get the transaction receipt
print("Waiting for transaction to finish...")
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print(f"Done! Contract deployed to {transaction_receipt.contractAddress}")
