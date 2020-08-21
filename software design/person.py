from address import Address
class Person:
    def __init__(self,first,last,dob,phone,address):
        self.first_name=first
        self.last_name=last
        self.date_o_birth=dob
        self.addresses=[]

        if isinstance(address,Address):
            self.addresses.append(address)
        elif isinstance(address,list):
            for entry in address:
                if not isinstance(entry,Address):
                    raise Error("Invalid Address..")
                self.addresses=address    
        else:
            raise Error("invalid address")

    def add_address(self,address):
        if not isinstance(address,Address):
            raise Error("invalid address")
        self.addresses.append(address)