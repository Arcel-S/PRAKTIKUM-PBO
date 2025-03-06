class Robot: #inisialisasi class robot
    def __init__(self, name, hp, attack): #inisialisasi parameter untuk menampung value attribut
        self.name = name          # nama robot
        self.hp = hp             # nyawa robot
        self.attack = attack     # kekuatan serangan biasa
        self.ulti_damage = 100   # kekuatan serangan ultimate
        self.action_count = 0    # menghitung jumlah aksi untuk syarat ultimate
        self.is_defending = False # status bertahan

    def attack_enemy(self, enemy, action_type): #aksi yang dilakukan oleh robot
        damage = 0   
        if action_type == "attack":
            damage = self.attack  # serangan biasa
        elif action_type == "ulti":
            if self.action_count >= 5:
                damage = self.ulti_damage
                self.action_count = 0   
            else:
                print(f"{self.name} tidak bisa menggunakan ulti, belum cukup aksi.")
                return
        
        # print damage awal sebelum dikurangi defense
        print(f"{self.name} menyerang {enemy.name} dengan {damage} kerusakan.")
        
        # kalo lawan defense, damage dikurangi 50%
        if enemy.is_defending:
            damage = damage // 2  
            print(f"{enemy.name} menahan serangan dan hanya menerima {damage} kerusakan!")
        else:
            print(f"{enemy.name} menerima {damage} kerusakan!")
            
        enemy.hp -= damage  # kurangi hp musuh

class Game(Robot):
    def __init__(self, robot1, robot2):
        super().__init__("GameMaster", 1000, 0)
        self.robot1 = robot1     # robot pertama
        self.robot2 = robot2     # robot kedua
        self.round = 1          # mulai dari ronde 1

    def display_status(self):
        # nampilin status kedua robot
        print(f"\nRound-{self.round} ==========================================================")
        print(f"{self.robot1.name} [HP: {self.robot1.hp} | ATK: {self.robot1.attack}]")
        print(f"{self.robot2.name} [HP: {self.robot2.hp} | ATK: {self.robot2.attack}]")

    def start_game(self):
        print("\nPertarungan Robot dimulai!")
        print("==========================")
        
        while self.robot1.hp > 0 and self.robot2.hp > 0:
            self.display_status()
            
            # nampilin pilihan dan minta input
            print(f"\nPilihan aksi: 1.Attack  2.Defense  3.Giveup  4.Ulti")
            action1 = int(input(f"{self.robot1.name}, pilih aksi (1-4): "))
            
            # kalo robot1 nyerah, langsung selesai
            if action1 == 3:
                print(f"\n{self.robot1.name} menyerah!")
                print(f"{self.robot2.name} memenangkan pertarungan!")
                break
            
            action2 = int(input(f"{self.robot2.name}, pilih aksi (1-4): "))
            
            # kalo robot2 nyerah, langsung selesai
            if action2 == 3:
                print(f"\n{self.robot2.name} menyerah!")
                print(f"{self.robot1.name} memenangkan pertarungan!")
                break

            # set status defense kalo robot milih bertahan
            if action1 == 2:
                self.robot1.is_defending = True
                print(f"{self.robot1.name} bersiap menahan serangan!")
            if action2 == 2:
                self.robot2.is_defending = True
                print(f"{self.robot2.name} bersiap menahan serangan!")

            print("\nHasil aksi:")
            # jalanin aksi yang dipilih (kecuali defense)
            if action1 != 2:
                self.robot1.action_count += 1
                if action1 == 1:
                    self.robot1.attack_enemy(self.robot2, "attack")
                elif action1 == 4:
                    self.robot1.attack_enemy(self.robot2, "ulti")

            if action2 != 2:
                self.robot2.action_count += 1
                if action2 == 1:
                    self.robot2.attack_enemy(self.robot1, "attack")
                elif action2 == 4:
                    self.robot2.attack_enemy(self.robot1, "ulti")

            # reset status defense di akhir ronde
            self.robot1.is_defending = False
            self.robot2.is_defending = False

            # cek ada yang kalah gak
            if self.robot1.hp <= 0:
                print(f"\n{self.robot2.name} memenangkan pertarungan!")
                break
            elif self.robot2.hp <= 0:
                print(f"\n{self.robot1.name} memenangkan pertarungan!")
                break

            self.round += 1  # next ronde

# bikin 2 robot buat main
robot1 = Robot("Ahmat Kopling", 500, 50)    # robot pertama: hp 500, attack 50
robot2 = Robot("Ucup Mber", 750, 40)        # robot kedua: hp 750, attack 40
game = Game(robot1, robot2)                  # mulai gamenya
game.start_game()                           # jalanin gamenya