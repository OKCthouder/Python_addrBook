# address book
import sys
import pickle

class Person:
    def __init__(self,name,phoneNum,addr):
        self.name = name
        self.phoneNum = phoneNum
        self.addr = addr

    def getName(self):
        return self.name

    def getPhoneNum(self):
        return self.phoneNum

    def getAddr(self):
        return self.addr

class addrBook:

    def __init__(self,option='add'):
        self.addressBook={}
        self.addressBookFile = 'AddrBook.data'
        f = open(self.addressBookFile, 'rb')
        try:
            self.addressBook = pickle.load(f)
        except:
            if option =='add':
                pass
            else:
                raise
                print('The addressBook is Empty.')
                f.close()
                sys.exit()
        finally:
            f.close()

    def addPerson(self,name,phoneNum,addr):
        try:
            somePerson = Person(name,phoneNum,addr)
            if self.addressBook.get(name):
                print("User %s already added to the addressBook." % name)
            else:
                self.addressBook[name] = somePerson
                print("Add Person Success.")
        except:
            raise
            print("There are some exceptions in add person.")

    def searchPerson(self,name):
        try:
            for nameFromBook,personFromBook in self.addressBook.items():
                if nameFromBook == name:
                    print("The address and phoneNumber of %s are %s and %s."\
                          % (name,personFromBook.getAddr(),personFromBook.getPhoneNum()))
                    return
            print("there is no user of %s." % name)
        except:
            print("There are some exceptions in searching person.")

    def delPerson(self,name):
        try:
            if self.addressBook.has_key(name):
                del self.addressBook[name]
                print("Delete Person Success.")
            else:
                print("there is no user of %s." % name)
        except:
            print("There are some exceptions in deleting person.")

    def __del__(self):
        try:
            f = open(self.addressBookFile,'wb')
            if not self.addressBook:
                pass
            else:
                pickle.dump(self.addressBook,f)
        except:
            raise
            print("Some exception occur when write data to file.")
        finally:
            f.close()

    def listAllPerson(self):
        try:
            for nameFromBook,personFromBook in self.addressBook.items():
                print("The address and phoneNumber of %s are %s and %s."\
                          % (nameFromBook,personFromBook.getAddr(),personFromBook.getPhoneNum()))
        except:
            print("There are some exceptions in listing person.")

helpDoc = '''All the command as follow:
    python addrBook1.py --help     : show help
    python addrBook1.py --version  : show version
    python addrBook1.py --add      : add user to addrBook
    python addrBook1.py --del      : delete user from addrBook
    python addrBook1.py --search   : search user from addrBook '''

def main():
    if len(sys.argv)<2:
        print('No Action Occur.')
        print(helpDoc)
        sys.exit()

    if sys.argv[1].startswith('--'):
        option = sys.argv[1][2:]
        if option=='help':
            print(helpDoc)
            sys.exit()

        elif option == 'version':
            print("version 0.0.2")
            sys.exit()

        AddrBookInst = addrBook(option)
        if option == 'add':
            name = input("Please intut the name:")
            phoneNum = input("Please intut the phone number:")
            addr = input("Please intut the address:")
            AddrBookInst.addPerson(name,phoneNum,addr)

        elif option=='del':
            name = input("Please intut the name that you want to del :")
            AddrBookInst.delPerson(name)

        elif option =='search':
            name = input("Please intut the name that you want to search :")
            AddrBookInst.searchPerson(name)

        elif option == 'list':   #hiden parameter :)
            AddrBookInst.listAllPerson()

        else:
            print("Parameter wrong, please check with help.")
        sys.exit()

if __name__ =="__main__":
    main()