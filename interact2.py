#!/usr/bin/env python3

# exec(open("setupcardano.py").read())

# este lo uso para mandar desde el creador
txargs0 = {"from": acc0, "gasPrice": web3.toWei('5', 'gwei'), "gas": 4000000}
# este lo uso para mandar desde el user
txargs1 = {"from": acc1, "gasPrice": web3.toWei('5', 'gwei'), "gas": 4000000}

with open("../Contratos/Compilado/Cardano2.abi") as contract_abi_file:
  contract_abi = json.load(contract_abi_file)
with open("../Contratos/Compilado/Cardano2.bin") as contract_bin_file:
  contract_bytecode = '0x' + contract_bin_file.read()

contract_address = "0xA9B76cD50B28bac8E0330d2A483c2eA6ab3b1Ab8"

# Una vez que calcule la direccion del contrato, se la asigno a la instancia
card2 = web3.eth.contract(address = contract_address, abi = contract_abi, bytecode = contract_bytecode)

nonce = web3.eth.getTransactionCount(acc0)

cardano_txn = card2.functions.setNum(
	  88,
  ).buildTransaction({
	  'gas': 200000,
	  'gasPrice': web3.toWei('5', 'gwei'),
	  'nonce': nonce,
  })


signed_txn = web3.eth.account.signTransaction(cardano_txn, private_key=private_key0)

tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
print(tx_hash)
