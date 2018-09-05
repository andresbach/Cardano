
with open("../../Contratos/Tests/Compilado/blockHash.abi") as contract_abi_file:
  contract_abi = json.load(contract_abi_file)
with open("../../Contratos/Tests/Compilado/blockHash.bin") as contract_bin_file:
  contract_bytecode = '0x' + contract_bin_file.read()

contract_address = "0x880f195C42dEe438671a6199e9271783f3E9Dd7b"
blockHash = web3.eth.contract(address = contract_address, abi = contract_abi, bytecode = contract_bytecode)

tx_hash = None

def actualiza(_accN):
	bh_txn = blockHash.functions.actualiza().buildTransaction({
		'gas': 1000000,
		'gasPrice': web3.toWei('5', 'gwei'),
		'nonce': web3.eth.getTransactionCount(acc[_accN])
	})
	#print(bh_txn)
	signed_txn = web3.eth.account.signTransaction(bh_txn, private_key=private_key[_accN])
	global tx_hash
	tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx_hash.hex())
	#print('Log:', web3.eth.waitForTransactionReceipt(tx_hash.hex()).logs[0]['data'])
	web3.eth.waitForTransactionReceipt(tx_hash.hex())

def lastH():
	return blockHash.functions.lastHash().call()

def blockN():
	return blockHash.functions.blockNumber().call()

def blockV():
	return blockHash.functions.blockValue().call()
