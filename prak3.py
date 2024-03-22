class Identitas:

    def __init__(self):
          #Identitas
        self.nama  = "Syahrul Arifin"
        self.nim   = "064002300031"
        self.studi = "Teknik Informatika"
        self.hobi  = "tidur sambil kayang"
    
    def nama(self):
        return  self .nama  #Mengembalikan nama 
    
    def fakultas(self):
        return self.studi #Mengembalikan fakultas
    
    def hobi(self):
        return self.hobi  #mengembalikan hobi
               
    def tampilan(self):  #Tampilan 
        
        print("Nama Saya adalah :" , self.nama)
        print("Nim saya adalah :" , self.nim)
        print("Saya dari fakultas :" , self.studi)
        print("Hobi saya adalah :", self.hobi)

   

def main():
    OIdentitas = Identitas()  #
    OIdentitas.tampilan()
    
    

if __name__ == "__main__":
    main()     