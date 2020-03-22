# Author (Created): Roger "Equah" Hürzeler
# Author (Modified): Roger "Equah" Hürzeler
# Date (Created): 12020.03.16 HE
# Date (Modified): 12020.03.22 HE
# License: apache-2.0


import equah.sblint


# [>] Interpreter
# [i] Nuntius interpreter.
class Interpreter :
    
    # [>] Initialize
    def __init__(self) :
        
        # [>] Interface
        # [i] Interface this interpreter uses to read and write.
        self.interface = None
        
        # [>] Element Types
        # [i] List of element types registered on this interpreter.
        self.element_types = []
        
        return
    
    # [>] Register Element Type
    # [i] Registers the given element type.
    # [P] {type} t_element => Type of element to register.
    def register_element_type(self, t_element) :
        
        self.element_types.append(t_element)
        
        return
    
    # [>] Get Element Type
    # [i] Returns the element class by given identity if egistered.
    # [P] {int} identity => Identity of element type to return.
    # [R] {type|NoneType} => The element class or None if not found.
    def get_element_type(self, identity) :
        
        for element_type in self.element_types :
            if element_type.IDENTITY == identity :
                return element_type
            pass
        
        return None
    
    # [>] Write Element
    # [i] Writes the given element.
    # [P] {Element} element => Element instance to write.
    # [R] {int} => Amount of written bytes.
    def write_element(self, element) :
        
        # [>] Write Single
        def write_single(c) :
            self.interface.write_single(c)
            return
        
        size = 0
        
        if self.interface.write_available() > 0 :
            
            size += equah.sblint.int_to_sbytes(element.IDENTITY, write_single)
            
            size += element.write()
            
            pass
        
        return size
    
    # [>] Read Element
    # [i] Reads the nextelement in input.
    # [R] {(int, Element)} => Element used to store read data.
    def read_element(self) :
        
        # [>] Read Single
        def read_single() :
            return self.interface.read_single()
        
        size = 0
        element = None
        
        if self.interface.read_available() > 0 :
            
            identity, identity_len = equah.sblint.sbytes_to_int(read_single)
            size += identity_len
            
            element_type = self.get_element_type(identity)
            
            if element_type != None :
                element = element_type(self)
                size += element.read()
                pass
            
            pass
        
        return (size, element)

# [>] Element
# [i] Superclass for element types.
class Element :
    
    # [>] Identity
    # [i] Defines the type identity.
    IDENTITY = 0
    
    # [>] Initialize
    def __init__(self, interpreter) :
        
        # [>] Interpreter
        # [i] Interpreter related to this element.
        self.interpreter = interpreter
        
        return
    
    # [>] Read
    # [i] Stub function to read this element.
    # [R] {int} => Amount of read bytes.
    def read(self) :
        
        return 0
    
    # [>] Write
    # [i] Stub function to write this element.
    # [R] {int} => Amount of written bytes.
    def write(self) :
        
        return 0


# [>] Interface
# [i] Superclass for interfaces.
class Interface :
    
    # [>] Initialize
    def __init__(self) :
        
        return
    
    # [>] Read Available
    # [i] Check input size.
    # [R] {int} => Amount of bytes available to read.
    def read_available(self) :
        
        return 0
    
    # [>] Read
    # [i] Read bytes from input.
    # [P] {bytearray|list} b => Bytearray to wrte read bytes into.
    # [P] {int} n => Amount of bytesto read.
    # [R] {int} => Amount of bytes that where read.
    def read(self, b, n) :
        
        return 0
    
    # [>] Read Single
    # [i] Function to read single char.
    # [R] {int} => Byte read from input.
    def read_single(self) :
        
        return 0x00
    
    # [>] Write Available
    # [i] Check if write is available.
    # [R] {int} => Amount of bytes which can be written.
    def write_available(self) :
        
        return 0
    
    # [>] Write
    # [i] Write bytes to output.
    # [P] {bytearray|bytes|list} b => Bytes to write.
    # [P] {int} n => Amount of bytes to write.
    # [R] {int} => Amount of bytes that where written.
    def write(self, b, n) :
        
        return 0
    
    # [>] Write Single
    # [i] Write single byte.
    # [P] {int} c => Byte to write.
    def write_single(self, c) :
        
        return

