#Nama : Nela Nurazizah
#NIM : 301230029
#Kelas : 2A
#Prodi : Teknik Informatika

# Soal no 1
print("PROGRAM DENGAN MENAMPILKAN SEBUAH STRING")
input_string = input("Kata yang dimasukkan adalah: ")

input_string = input_string.capitalize()

for letter in input_string:
    print(letter)
print("----------------------------------------------------\n")


#Soal no 2
print("PROGRAM DENGAN MENAMPILKAN SEBUAH PERULANGAN PIRAMIDA DENGAN MENAMPILKAN KARAKTER EMOJI SMILE")
string =" "
bar = 1

x = int (input("Masukkan angka :"))

#Looping baris
while bar <= x :
    kol = bar

    #Looping kolom
    while kol > 0 :
        string = string + "\U0001f600"
        kol = kol - 1
    
    string = string + "\n"
    bar = bar + 1
print (string)


for i in range(x):
    print(' ' * (x - i - 1) + '\U0001f600' * (1 * i + 1))
print("----------------------------------------------------\n")


#Soal no 3
print("PROGRAM DENGAN MENAMPILKAN NILAI RATA - RATA")
numbers_str = input("Masukkan nilai : ")
numbers = [int(x) for x in numbers_str.split(",")]
average = sum(numbers) / len(numbers)
print("Nilai:", str(numbers)[1:-1])
print("Nilai rata-rata:", round(average, 1))
print("----------------------------------------------------\n")


#Soal no 4
print("PROGRAM DENGAN MENAMPILKAN NILAI TERENDAH, TERBESAR, DAN MEDIAN DARI BILANGAN")
numbers_str = input("Masukkan bilangan : ")
numbers = [int(x) for x in numbers_str.split(",")]
numbers.sort()
minimum = numbers[0]
maximum = numbers[-1]
median = numbers[len(numbers) // 2]
print("Bilangan:", str(numbers)[1:-1])
print("Nilai Terendah:", minimum)
print("Nilai Median:", median)
print("Nilai Terbesar:", maximum)
print("----------------------------------------------------\n")

#Soal no 5
print("PROGRAM MESIN ATM")
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Dana tidak cukup")
            return None
        else:
            self.balance -= amount
            return self.balance

def main():
    account = BankAccount()
    pin = 1234
    print("Welcome to the ATM!")
    while True:
        user_input = input("Masukkan PIN: ")
        if user_input == str(pin):
            print("Login successful!")
            while True:
                print("\nATM Menu:")
                print("1. Informasi Saldo")
                print("2. Penarikan tunai")
                print("3. Nabung")
                print("4. Exit")
                user_input = input("Pilih menu yang diinginkan: ")
                if user_input == "1":
                    print("Isi saldo: Rp.", account.balance)
                elif user_input == "2":
                    print("Jumlah nominal penarikan sebesar: 50000, 100000, 2500000, 500000, 1000000")
                    amount = float(input("Masukkan jumlah penarikan Anda: "))
                    if account.withdraw(amount) is not None:
                        print("Withdrawal successful! Sisa saldo rekening Anda: Rp.", account.balance)
                elif user_input == "3":
                    amount = float(input("Masukkan nominal uang yang Anda tabung: "))
                    account.deposit(amount)
                    print("Deposit successful! Saldo Anda: Rp.", account.balance)
                elif user_input == "4":
                    print("Thank you for using the ATM!")
                    break
                else:
                    print("Input tidak sesuai")
        else:
            print("PIN yang dimasukkan salah")
            continue
        break

if __name__ == "__main__":
    main()
print("----------------------------------------------------\n")