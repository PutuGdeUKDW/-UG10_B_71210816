bil = int(input("Masukkan angka: "))

bilangan1 = bil%2
bilangan2 = bil%3
bilangan5 = bil%5
bilangan10 = bil%10

if (bilangan1 == 0 and bilangan2 !=0 and(bilangan5 !=0 and bilangan10 == 0) ) :
    print("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3? Jawab: Ya")
    print("Apakah bilangan tersebut tidak habis dibagi dengan 5 atau habis dibagi 10?: IYA DONG")
elif (bilangan1 == 0 and bilangan2 !=0 and(bilangan5 !=0 and bilangan10 != 0) ) :
    print("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3? Jawab:Ya")
    print("Apakah bilangan tersebut tidak habis dibagi dengan 5 atau habis dibagi 10?: TIDAK")
elif (bilangan1 != 0 and bilangan2 ==0) :
    print("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. Program dihentikan")
elif (bilangan1 != 0 and bilangan2 !=0) :
    print("Bilangan tersebut tidak habis dibagi 2 dan tidak habis dibagi 3. Program dihentikan")
else: 
    print ("Input Error")
