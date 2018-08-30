def encodeC(_extra, _to, _gas, _gasPrice, _value,):
#	print('sendTransaction(to =', ('0x'+('%x' % _to)), ', gas =', _gas, ', gasPrice =', _gasPrice, ', value =', _value, ', data =', 123, ')')
#	print('sendTransaction(to =', _to, ', gas =', _gas, ', gasPrice =', _gasPrice, ', value =', _value, ', data =', _extra['data'], ')')
	print('sendTransaction(to =', '0x{0:0{1}X}'.format(_to,40), ', gas =', _gas, ', gasPrice =', _gasPrice, ', value =', _value, ', data =', _extra['data'], ')')
	pass

# sendTransaction(to = 0x02F62A1e10C3ED6eA170856f505703f834D49779, gas = 100000, gasPrice = 5000000000, value = 0, data = 0xcd16ecbf0000000000000000a)

# la uso asi, donde _extra tengo que darselo en string ya (o sea con comillas si no lo es ya).
# La parte de data no necesito forzar hex ya que siempre empieza con un numero distinto de cero
# encodeC(card.functions.setNum(88).buildTransaction(), '0x02F62A1e10C3ED6eA170856f505703f834D49779', 100000, 5*10**9, 0)
