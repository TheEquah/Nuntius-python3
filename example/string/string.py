# Author (Created): Roger "Equah" Hürzeler
# Date (Created): 12020.03.22 HE
# License: apache-2.0

import equah.sblint

import equah.nuntius

# [>] My Interface
# [i] Example of a Nuntius interface.
class MyInterface (equah.nuntius.Interface) :
	
	def __init__(self) :
		equah.nuntius.Interface.__init__(self)
		
		# [>] Input Output
		# [i] A bytearray containing the written bytes.
		self.io = bytearray(1024)
		
		# [i] Current read and write position in IO.
		self.read_pos = 0
		self.write_pos = 0
		
		return
	
	def read_available(self) :
		return len(self.io) - self.read_pos
	
	def read(self, c, n) :
		_a = 0
		while (_a < n and len(self.io) > _a) :
			c[_a] = self.io[self.read_pos + _a]
			_a += 1
			pass
		self.read_pos += _a
		return _a
	
	def read_single(self) :
		self.read_pos += 1
		return self.io[self.read_pos - 1]
	
	def write_available(self) :
		return len(self.io) - self.write_pos
	
	def write(self, c, n) :
		_a = 0
		while (_a < n and len(c) > _a) :
			self.io[self.write_pos + _a] = c[_a]
			_a += 1
			pass
		self.write_pos += _a
		return _a
	
	def write_single(self, c) :
		self.io[self.write_pos] = c
		self.write_pos += 1
		return


# [>] Nuntius Element - My String
# [i] Example string element class.
class NE_MyString (equah.nuntius.Element) :
	
	IDENTITY = 1
	
	def __init__(self, interpreter) :
		equah.nuntius.Element.__init__(self, interpreter)
		
		# [>] String
		# [i] String stored in this element.
		self.str = ""
		
		return
	
	def read(self) :
		
		read = bytearray()
		
		next_byte = self.interpreter.interface.read_single()
		while next_byte != 0x00 :
			read.append(next_byte)
			next_byte = self.interpreter.interface.read_single()
			pass
		
		self.str = read.decode("ascii")
		
		return 0
	
	def write(self) :
		
		pos = 0
		
		write = self.str.encode("ascii")
		
		self.interpreter.interface.write(write, len(write))
		self.interpreter.interface.write_single(0x00)
		
		return 0


# [>] Main
if __name__== "__main__":
	
	# [i] Initialize theinterpreter and interface.
	my_interpreter = equah.nuntius.Interpreter()
	my_interpreter.interface = MyInterface()
	
	# [i] Register my string element type.
	my_interpreter.register_element_type(NE_MyString)
	
	# [i] Create a string element and set a string value.
	my_element = NE_MyString(my_interpreter)
	my_element.str = "Hello World"
	
	# [i] Write the string element.
	my_interpreter.write_element(my_element)
	print("WRITE:", my_element.str)
	
	# [i] Print content in IO.
	print("IO:", my_interpreter.interface.io)
	
	# [i] Read the written string element.
	element_read = my_interpreter.read_element()[1]
	print("READ:", element_read.str)
	
	pass

