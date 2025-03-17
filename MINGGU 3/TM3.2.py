import random

class Father:
    def __init__(self, nama, blood_type):
        self.nama = nama
        self.blood_types = self._validate_blood_type(blood_type)
    
    def _validate_blood_type(self, blood_type):
        valid_types = {'A', 'B', 'O', 'AB'}
        if blood_type not in valid_types:
            raise ValueError("Golongan darah harus A, B, AB, atau O")
        if blood_type == 'O':
            return ['O', 'O']
        elif blood_type == 'A':
            return ['A', 'O']
        elif blood_type == 'B':
            return ['B', 'O']
        elif blood_type == 'AB':
            return ['A', 'B']

    def __str__(self):
        return f"{self.nama}: Golongan darah {self.blood_types[0]}"

class Mother:
    def __init__(self, nama, blood_type):
        self.nama = nama
        self.blood_types = self._validate_blood_type(blood_type)
    
    def _validate_blood_type(self, blood_type):
        valid_types = {'A', 'B', 'O', 'AB'}
        if blood_type not in valid_types:
            raise ValueError("Golongan darah harus A, B, AB, atau O")
        if blood_type == 'O':
            return ['O', 'O']
        elif blood_type == 'A':
            return ['A', 'O']
        elif blood_type == 'B':
            return ['B', 'O']
        elif blood_type == 'AB':
            return ['A', 'B']

    def __str__(self):
        return f"{self.nama}: Golongan darah {self.blood_types[0]}"

class Child:
    def __init__(self, nama, father, mother):
        self.nama = nama
        self.father_allele = random.choice(father.blood_types)
        self.mother_allele = random.choice(mother.blood_types)
        self.blood_type = self._determine_blood_type()
    
    def _determine_blood_type(self):
        alleles = sorted([self.father_allele, self.mother_allele])
        if alleles == ['O', 'O']:
            return 'O'
        elif alleles in (['A', 'O'], ['A', 'A']):
            return 'A'
        elif alleles in (['B', 'O'], ['B', 'B']):
            return 'B'
        elif alleles == ['A', 'B']:
            return 'AB'
    
    def __str__(self):
        return f"{self.nama}: Golongan darah {self.blood_type}"

if __name__ == "__main__":
    gdAyah = input("Masukkan golongan darah ayah (A/B/AB/O): ").upper()
    gdIbu = input("Masukkan golongan darah ibu (A/B/AB/O): ").upper()
    
    ayah = Father("Bapak Ahmad", gdAyah)
    ibu = Mother("Ibu Siti", gdIbu)
    anak = Child("Anak Gatot", ayah, ibu)

    print("\nGolongan Darah Keluarga:")
    print(ayah)
    print(ibu)
    print(anak)
