
with open("../../Contratos/Tests/Compilado/suicida.abi") as contract_abi_file:
  contract_abi = json.load(contract_abi_file)
with open("../../Contratos/Tests/Compilado/suicida.bin") as contract_bin_file:
  contract_bytecode = '0x' + contract_bin_file.read()

contract_address = "0x7Cf47ac335f5c46B3aAe2C4dC3678D7F9CbF10ad"
suicida = web3.eth.contract(address = contract_address, abi = contract_abi, bytecode = contract_bytecode)

tx_hash = None

def matame(_accN):
	balance_inicial = web3.eth.getBalance(acc[_accN])


	sd_txn = suicida.functions.matame().buildTransaction({
		'gas': 1000000,
		'gasPrice': web3.toWei('5', 'gwei'),
		'nonce': web3.eth.getTransactionCount(acc[_accN])
	})
	#print(bh_txn)
	signed_txn = web3.eth.account.signTransaction(sd_txn, private_key=private_key[_accN])
	global tx_hash
	tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx_hash.hex())

	web3.eth.waitForTransactionReceipt(tx_hash.hex())
	balance_final = web3.eth.getBalance(acc[_accN])
	print('Diferencia de balances: ', balance_final-balance_inicial, balance_inicial, balance_final)

	#print('Log:', web3.eth.waitForTransactionReceipt(tx_hash.hex()).logs[0]['data'])
	return web3.eth.getTransactionReceipt(tx_hash.hex())


def mandarPlata(_to, _value, _accN):
	signed_txn = web3.eth.account.signTransaction(dict(
    		nonce = web3.eth.getTransactionCount(acc[_accN]),
    		gasPrice = web3.toWei('5', 'gwei'),
    		gas = 50000,
    		to = _to,
    		value = _value,
    		#data=b'',
			),
			private_key[_accN],
		)
	global tx_hash
	tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx_hash.hex())
	web3.eth.waitForTransactionReceipt(tx_hash)

def duenio():
	return suicida.functions.owner().call()
