
with open("../Contratos/Compilado/CoinFabrikToken.abi") as contract_abi_file:
  contract_abi = json.load(contract_abi_file)
with open("../Contratos/Compilado/CoinFabrikToken.bin") as contract_bin_file:
  contract_bytecode = '0x' + contract_bin_file.read()

contract_address = "0xAe08d9EB886795FdEF16c93A77dFeC68B69d4AbB"
cfToken = web3.eth.contract(address = contract_address, abi = contract_abi, bytecode = contract_bytecode)

tx_hash = None
gas = 150000
gasPrice = web3.toWei('5', 'gwei')
#gasPrice = 1

def duenio():
	return cfToken.functions.owner().call()

def empresa():
	return cfToken.functions.name().call()

def getDuenio():
	return cfToken.functions.getON().call()

def setDuenio(nombre,_accN):

	unsigned_txn = cfToken.functions.setON(nombre).buildTransaction({
		'gas': gas,
		'gasPrice': gasPrice,
		'nonce': web3.eth.getTransactionCount(acc[_accN])
	})
	#print(bh_txn)
	signed_txn = web3.eth.account.signTransaction(unsigned_txn, private_key=private_key[_accN])
	global tx_hash
	tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx_hash.hex())

	return web3.eth.waitForTransactionReceipt(tx_hash.hex())

def balance(_account):
	return cfToken.functions.balanceOf(_account).call()

def transferir(_to, _value, _accN):

	unsigned_txn = cfToken.functions.transfer(_to, _value).buildTransaction({
		'gas': gas,
		'gasPrice': gasPrice,
		'nonce': web3.eth.getTransactionCount(acc[_accN])
	})
	#print(bh_txn)
	signed_txn = web3.eth.account.signTransaction(unsigned_txn, private_key=private_key[_accN])
	global tx_hash
	tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx_hash.hex())

	#print('Log:', web3.eth.waitForTransactionReceipt(tx_hash.hex()).logs[0]['data'])
	return web3.eth.waitForTransactionReceipt(tx_hash.hex())

def mandarPlata(_to, _value, _accN):
	signed_txn = web3.eth.account.signTransaction(dict(
    		nonce = web3.eth.getTransactionCount(acc[_accN]),
    		gasPrice = gasPrice,
    		gas = 25000,
    		to = _to,
    		value = _value,
    		#data=b'',
			),
			private_key[_accN],
		)
	global tx_hash
	tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx_hash.hex())
	return web3.eth.waitForTransactionReceipt(tx_hash)

def matate(_accN):

	unsigned_txn = cfToken.functions.destroy().buildTransaction({
		'gas': gas,
		'gasPrice': gasPrice,
		'nonce': web3.eth.getTransactionCount(acc[_accN])
	})
	#print(bh_txn)
	signed_txn = web3.eth.account.signTransaction(unsigned_txn, private_key=private_key[_accN])
	global tx_hash
	tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx_hash.hex())

	return web3.eth.waitForTransactionReceipt(tx_hash.hex())
