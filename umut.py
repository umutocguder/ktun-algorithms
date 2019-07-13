    """
        171220036.txt metin dosyasını LZW sıkıştırma algoritmasına uygun olarak sıkıştıracaktır. Programınız oluşan sözcük yapısını ekrana yazacaktır (l). Aynı zamanda sıkıştırılmış halini ekrana (k) ve 171220036_lzw.txt dosyasına (k'yı) yazacaktır.
        
        171220036_lzw.txt  adındaki sıkıştırılmış dosyanın LZW algoritmasına göre açılmış halini(k) ekrana ve  171220036_orijinal.txt dosyasına(k'yı) yazacaktır. oluşan sözlük yapısını(l) ekrana yazacaktır.
        
        Düz metin: ABABCAB
        Sıkıştrılmış hali(k): 65 66 256 67 256
        Sözcük Yapısı(l)
        
        AB: 256
        BA: 257
        ABC: 258
        CA: 259
        
        17120036_alg_odev3.rar formatında.
    """

karakterler = ""
karakter = ''
String1 = ""
umut = {}
counter = 256

def createumut(umut):
    global counter, karakterler
    for i in range(len(karakterler)):
        if karakterler[i] in umut.values():
            pass
        else:
            umut[ord(karakterler[i])] = karakterler[i]

def findumut(Findd):

    for key,value in umut.items():
        if value == Findd:
            return key


def readFromFile():
    global karakterler
    with open("171220036.txt","r",encoding="utf-8") as file:
        karakterler = file.read()

    print("İlk metin: " + karakterler)

def LZW():
    global String1, counter, karakterler
    print("Sıkıstırılmıs : ", end="")
    newCounter= 0
    while newCounter < len(karakterler):
        chr = karakterler [newCounter]
        if String1 + chr in umut.values():
            String1 = String1 + chr
            newCounter = newCounter + 1
        else:
            key = findumut(String1)
            print(key, end=" ")
            with open("171220036_lzw.txt","a") as file:
                file.write(str(key) + " ")
            umut[counter] = String1 + chr
            String1 = chr
            counter = counter + 1
            newCounter = newCounter + 1
    key = findumut(String1)
    print(key)
    with open("171220036_lzw.txt", "a") as file:
        file.write(str(key) + " ")

def lzwread():
    with open("171220036_lzw.txt","r", encoding= "utf-8") as file:
        line = file.read()
        line = line[:-1]
        list = line.split(" ")
        print("Decodelanmıs: " , end="")
        for i in list:
            for key,value in umut.items():
                if str(key) == str(i):
                    with open("171220036_original.txt", "a") as file:
                        file.write(str(value) + "")
                    print(value, end="")

readFromFile()
print()
createumut(umut)
LZW()
print()
lzwread()
print()
print()
print(umut)
