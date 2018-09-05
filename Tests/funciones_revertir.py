
with open("../../Contratos/Tests/Compilado/revertir.abi") as contract_abi_file:
  contract_abi = json.load(contract_abi_file)
with open("../../Contratos/Tests/Compilado/revertir.bin") as contract_bin_file:
  contract_bytecode = '0x' + contract_bin_file.read()

contract_address = "0xD9eCB316aCbEFf81C4F957A2D46083B92e0063Be"
revierte = web3.eth.contract(address = contract_address, abi = contract_abi, bytecode = contract_bytecode)

tx_hash = None

def llamame(_num, _accN):
	balance_inicial = web3.eth.getBalance(acc[_accN])


	bh_txn = revierte.functions.llamame(_num).buildTransaction({
		'gas': 1000000,
		'gasPrice': web3.toWei('5', 'gwei'),
		'nonce': web3.eth.getTransactionCount(acc[_accN])
	})
	#print(bh_txn)
	signed_txn = web3.eth.account.signTransaction(bh_txn, private_key=private_key[_accN])
	global tx_hash
	tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx_hash.hex())

	web3.eth.waitForTransactionReceipt(tx_hash.hex())
	balance_final = web3.eth.getBalance(acc[_accN])
	print('Diferencia de balances: ', balance_final-balance_inicial, balance_inicial, balance_final)

	#print('Log:', web3.eth.waitForTransactionReceipt(tx_hash.hex()).logs[0]['data'])
	return web3.eth.getTransactionReceipt(tx_hash.hex())
