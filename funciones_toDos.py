
with open("../Contratos/Compilado/TodoList.abi") as contract_abi_file:
  contract_abi = json.load(contract_abi_file)
with open("../Contratos/Compilado/TodoList.bin") as contract_bin_file:
  contract_bytecode = '0x' + contract_bin_file.read()

contract_address = "0x412F46d9D27356260B47AF0D0480ea34814f3991"
todos = web3.eth.contract(address = contract_address, abi = contract_abi, bytecode = contract_bytecode)

tx_hash = None
gas = 1000000
gasPrice = web3.toWei('5', 'gwei')
#gasPrice = 1

def duenio():
	return todos.functions.owner().call()

def anotaciones(_accN):
	if todos.functions.overIds(acc[_accN]).call():
		last = 5
	else:
		last = todos.functions.lastIds(acc[_accN]).call()
	for i in range(last):
		print(todos.functions.todos(acc[_accN],i).call())

def addTodo(contenido,_accN):

	unsigned_txn = todos.functions.addTodo(contenido).buildTransaction({
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

def markTodoAsCompleted(Id,_accN):

	unsigned_txn = todos.functions.markTodoAsCompleted(Id).buildTransaction({
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

def matame(_accN):

	unsigned_txn = todos.functions.matame().buildTransaction({
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
