
with open("../Contratos/Compilado/TicTacToe2.abi") as contract_abi_file:
  contract_abi = json.load(contract_abi_file)
with open("../Contratos/Compilado/TicTacToe2.bin") as contract_bin_file:
  contract_bytecode = '0x' + contract_bin_file.read()

contract_address = "0xDDB0F27773BC7bA619b43F7FABC631357857983F"
tic = web3.eth.contract(address = contract_address, abi = contract_abi, bytecode = contract_bytecode)

#tx_hash = None
#ticket = None
gas = 200000
gasPrice = web3.toWei('5', 'gwei')
#gasPrice = 1

def player1():
	return tic.functions.player1().call()

def player2():
	return tic.functions.player2().call()

def estado():
	return tic.functions.gameActive().call()

def costo():
	return tic.functions.gameCost().call()

def tablero():
	#board = list(tic.functions.getBoard().call())
	board = tic.functions.getBoard().call()
	for i in range(3):
		for j in range(3):
			if (board[i][j] == acc0):
				board[i][j] = 1
			elif (board[i][j] == acc1):
				board[i][j] = 2
			else:
				board[i][j] = 0
	print('\n',board[0],'\n',board[1],'\n',board[2],'\n')

	global tx_hash


	try:
		player = tic.events.NextPlayer().processReceipt(web3.eth.getTransactionReceipt(tx_hash.hex()))[0]['args'].player
	except IndexError: player = None

	try:
		winner = tic.events.GameOverWithWin().processReceipt(web3.eth.getTransactionReceipt(tx_hash.hex()))[0]['args'].winner
	except IndexError: winner = None


	if (player is None):
		None
	else:
		print('Ahora le toca a', player)

	if (winner is None):
		None
	else:
		print('El que gano fue', winner)


def entrar(_accN):

	unsigned_txn = tic.functions.joinGame().buildTransaction({
		'gas': gas,
		'gasPrice': gasPrice,
		'nonce': web3.eth.getTransactionCount(acc[_accN]),
		'value': 10
	})
	#print(bh_txn)
	signed_txn = web3.eth.account.signTransaction(unsigned_txn, private_key=private_key[_accN])
	global tx_hash
	tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx_hash.hex())

	global ticket
	ticket = web3.eth.waitForTransactionReceipt(tx_hash.hex())

	try:
		player = tic.events.NextPlayer().processReceipt(web3.eth.getTransactionReceipt(tx_hash.hex()))[0]['args'].player
	except IndexError: player = None

	if (player is None):
		None
	else:
		print('Ahora le toca a', player)

	#return ticket


def ficha(_x, _y, _accN):

	unsigned_txn = tic.functions.setStone(_x, _y).buildTransaction({
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
	global ticket
	ticket = web3.eth.waitForTransactionReceipt(tx_hash.hex())
	tablero()

	#return web3.eth.waitForTransactionReceipt(tx_hash.hex())


def salirse(_accN):

	unsigned_txn = tic.functions.emergecyCashout().buildTransaction({
		'gas': gas,
		'gasPrice': gasPrice,
		'nonce': web3.eth.getTransactionCount(acc[_accN])
	})
	#print(bh_txn)
	signed_txn = web3.eth.account.signTransaction(unsigned_txn, private_key=private_key[_accN])
	global tx_hash
	tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx_hash.hex())

	global ticket
	ticket = web3.eth.waitForTransactionReceipt(tx_hash.hex())

	#return web3.eth.waitForTransactionReceipt(tx_hash.hex())
