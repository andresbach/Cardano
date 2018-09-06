#!/usr/bin/env python3

# exec(open("../Setups/cardano.py").read())

# desde que cuenta deployo
_accN = 0

# este lo uso para mandar desde el creador
txargs = {
	"from": acc[_accN],
	"gasPrice": web3.toWei('5', 'gwei'),
#	"gasPrice": 1,
	"gas": 4000000,
	"nonce": web3.eth.getTransactionCount(acc[_accN])
	}

with open("../Contratos/Compilado/TodoList.abi") as contract_abi_file:
  contract_abi = json.load(contract_abi_file)
with open("../Contratos/Compilado/TodoList.bin") as contract_bin_file:
  contract_bytecode = '0x' + contract_bin_file.read()

# este solo construye la instancia, pero no deploya
todos = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
# este es el que deploya desde acc0
unsigned_txn = todos.constructor().buildTransaction(transaction=txargs)

signed_txn = web3.eth.account.signTransaction(unsigned_txn, private_key=private_key[_accN])

tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

# esta predice donde va a estar el contrato.
contract_address = generate_contract_address(acc[_accN], web3.eth.getTransaction(tx_hash).nonce)
#contract_address = "0x02F62A1e10C3ED6eA170856f505703f834D49779"

# Una vez que calcule la direccion del contrato, se la asigno a la instancia
todos = web3.eth.contract(address = contract_address, abi = contract_abi, bytecode = contract_bytecode)

print("Deployment hash:", tx_hash.hex())
print("Deployment address:", todos.address)
print("Please wait for the contract to be mined...")
# Esto hace que espere a ser minado y le asigna a ticket los valores del recibo
ticket = web3.eth.waitForTransactionReceipt(tx_hash.hex());


# de ticket tambien puedo sacar la address como
# ticket.contractAddress
