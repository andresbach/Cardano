#!/usr/bin/env python3

# exec(open("setupcardano.py").read())

# este lo uso para mandar desde el creador
txargs0 = {"from": acc0, "gasPrice": 5000000000, "gas": 4000000}
# este lo uso para mandar desde el user
txargs1 = {"from": acc1, "gasPrice": 5000000000, "gas": 4000000}

with open("../Contratos/Compilado/Cardano.abi") as contract_abi_file:
  contract_abi = json.load(contract_abi_file)
with open("../Contratos/Compilado/Cardano.bin") as contract_bin_file:
  contract_bytecode = '0x' + contract_bin_file.read()

contract_address = "0x02F62A1e10C3ED6eA170856f505703f834D49779"

# Una vez que calcule la direccion del contrato, se la asigno a la instancia
card = web3.eth.contract(address = contract_address, abi = contract_abi, bytecode = contract_bytecode)

nonce = web3.eth.getTransactionCount(acc1)

cardano_txn = card.functions.setNum(
	  100,
  ).buildTransaction({
	  'gas': 100000,
	  'gasPrice': web3.toWei('5', 'gwei'),
	  'nonce': nonce,
  })

signed_txn = web3.eth.account.signTransaction(cardano_txn, private_key=private_key)

web3.eth.sendRawTransaction(signed_txn.rawTransaction)
