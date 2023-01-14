

class rsa_ex(object):

    def __init__(self):
        
        self.message = str(input("Enter a message: "))
        self.p = int(input("Enter a Prime Number: "))
        self.q = int(input("Enter a Prime Number: "))
        self.N = self.p * self.q
        self.phi_N = self.phi()
        self.e = self.gen_e()
        self.d = self.modinv(self.e,self.phi_N)
        self.cipher = self.cypher(self.message)
        self.decrypt = self.decrypt(self.cipher)

    def __str__(self):
        return (f"p:{self.p} " f"q:{self.q} " f"N:{self.N} " f"Phi N:{self.phi_N} " f"E:{self.e} " f"D: {self.d}"  f"\nmessage: {self.message} " 
        f"\ncipher: {self.cipher} " f"\ndecrypt: {self.decrypt}") 
        

    def phi(self):
        return (self.p-1)*(self.q-1)

    def factorize(self,num):
        factors = []

        for i in range(2,num//2 +1):
            if(num%i == 0):
                factors.append(i)
                
        factors.append(num)
        return factors 

    def gen_e(self):
        n_facts = self.factorize(self.N)
        phi_n_facts = self.factorize(self.phi_N)

        for i in range(2,self.phi_N):
            i_facts = self.factorize(i)
            flag = True

            for j in i_facts:
                if j in n_facts or j in phi_n_facts:
                    flag = False

            if flag: 
                return i 

    

    def ext_euclid(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.ext_euclid(b % a, a)
            return g, x - (b // a) * y, y


    def modinv(self, a, m):
        g, x, y = self.ext_euclid(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def cypher(self, message):
        cipher = []

        for char in message:
            cipher.append(((ord(char)**self.e) % self.N))
        
        return cipher

    def decrypt(self, cipher):
        orig = ""
        
        for index in cipher:
            orig += chr((index**self.d) % self.N)

        return orig
   
print(rsa_ex())
