#!/usr/bin/env python3

# exec(open("../Setups/cardano.py").read())

nonce0 = web3.eth.getTransactionCount(acc0)
nonce1 = web3.eth.getTransactionCount(acc1)

# este lo uso para mandar desde el creador
txargs0 = {"from": acc0, "gasPrice": web3.toWei('5', 'gwei'), "gas": 4000000, "nonce": nonce0}
# este lo uso para mandar desde el user
txargs1 = {"from": acc1, "gasPrice": web3.toWei('5', 'gwei'), "gas": 4000000, "nonce": nonce1}

with open("../../Contratos/Tests/Compilado/suicida.abi") as contract_abi_file:
  contract_abi = json.load(contract_abi_file)
with open("../../Contratos/Tests/Compilado/suicida.bin") as contract_bin_file:
  contract_bytecode = '0x' + contract_bin_file.read()

# este solo construye la instancia, pero no deploya
suicida = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
# este es el que deploya desde acc0
sd_txn = suicida.constructor().buildTransaction(transaction=txargs0)

signed_txn = web3.eth.account.signTransaction(sd_txn, private_key=private_key0)

tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

# esta predice donde va a estar el contrato.
contract_address = generate_contract_address(acc0, web3.eth.getTransaction(tx_hash).nonce)
#contract_address = "0x02F62A1e10C3ED6eA170856f505703f834D49779"

# Una vez que calcule la direccion del contrato, se la asigno a la instancia
suicida = web3.eth.contract(address = contract_address, abi = contract_abi, bytecode = contract_bytecode)

print("Deployment hash:", tx_hash.hex())
print("Deployment address:", suicida.address)
print("Please wait for the contract to be mined...")
# Esto hace que espere a ser minado y le asigna a ticket los valores del recibo
ticket = web3.eth.waitForTransactionReceipt(tx_hash.hex());


# de ticket tambien puedo sacar la address como
# ticket.contractAddress
