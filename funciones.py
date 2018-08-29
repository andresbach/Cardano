
with open("./Contratos/Compilado/Cardano2.abi") as contract_abi_file:
  contract_abi = json.load(contract_abi_file)
with open("./Contratos/Compilado/Cardano2.bin") as contract_bin_file:
  contract_bytecode = '0x' + contract_bin_file.read()

contract_address = "0xAD6438a3d77D2Dd68fBbcEA68635a6a991c9C7e0"
card2 = web3.eth.contract(address = contract_address, abi = contract_abi, bytecode = contract_bytecode)

tx_hash = None

def _setNum(_num, _accN):
	cardano_txn = card2.functions.setNum(
		_num,
	).buildTransaction({
		'gas': 200000,
		'gasPrice': web3.toWei('5', 'gwei'),
		'nonce': web3.eth.getTransactionCount(acc[_accN]),
	})
	print(cardano_txn)
	signed_txn = web3.eth.account.signTransaction(cardano_txn, private_key=private_key[_accN])
	global tx_hash
	tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx_hash.hex())
	print('Log:', web3.eth.waitForTransactionReceipt(tx_hash.hex()).logs[0]['data'])

def _getNum():
	return card2.functions.num().call()

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






with open("../Contratos/Compilado/CoinFlip.abi") as contract_abi_file:
  contract_abi = json.load(contract_abi_file)
with open("../Contratos/Compilado/CoinFlip.bin") as contract_bin_file:
  contract_bytecode = '0x' + contract_bin_file.read()

contract_address = "0xC590438D9f6D876242174CdC587E6b7f5e139AB3"
flip = web3.eth.contract(address = contract_address, abi = contract_abi, bytecode = contract_bytecode)

def flipCoin(_estimo, _accN):
	flip_txn = flip.functions.flip(_estimo).buildTransaction({
		'gas': 1000000,
		'gasPrice': web3.toWei('5', 'gwei'),
		'nonce': web3.eth.getTransactionCount(acc[_accN])
	})
	print(flip_txn)
	signed_txn = web3.eth.account.signTransaction(flip_txn, private_key=private_key[_accN])
	global tx_hash
	tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx_hash.hex())
	print('Log:', web3.eth.waitForTransactionReceipt(tx_hash.hex()).logs[0]['data'])

def wins():
	return flip.functions.consecutiveWins().call()
