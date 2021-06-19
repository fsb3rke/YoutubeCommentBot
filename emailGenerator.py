import random

import emailGenerateBrowser

emailcik = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"
]
passwordcik = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"
]
alfabe = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
isimler = [
    "Sedat", "Kemal", "Murat", "Ekine", "Ekrem", "Burak"
]
isim = [
    "aaaaa"
]
soyisimler = [
    "Sahin", "Guclu", "Alkac", "Ersen", "Erdem", "Tekin"
]
soyisim = [
    "aaaaa"
]

tirnak = '"'
file1p = open("cakmaDATABASE.txt", "a")
file1p.write("\n\n\n\n # --------------------------\n\n\n\n")
file1p.close()
"""

file2p = open("database.py", "a")
file2p.write("\n\n\n\n # --------------------------\n\n\n\n")
file2p.close()

file2pp = open("database.py", "a")
file2pp.write("import databaseicinkayit as dbik")
file2pp.close()
"""

for k in range(20+1):
    for i in range(len(emailcik)):
        alfabe_mixer_email = random.shuffle(alfabe)
        emailcik[i] = alfabe[i]
        formatted_emailcik = emailcik[0] + emailcik[1] + emailcik[2] + emailcik[3] + emailcik[4] + emailcik[5] + emailcik[6] + emailcik[7] + emailcik[8] + emailcik[9] + emailcik[10] + emailcik[11]
        formatted_email = formatted_emailcik

    for j in range(len(passwordcik)):
        alfabe_mixer_password = random.shuffle(alfabe)
        passwordcik[j] = alfabe[j]
        formatted_passwordcik = passwordcik[0] + passwordcik[1] + passwordcik[2] + passwordcik[3] + passwordcik[4] + passwordcik[5] + passwordcik[6] + passwordcik[7] + passwordcik[8] + passwordcik[9]
        formatted_password = formatted_passwordcik


    isimler_mixer = random.choice(isimler)
    formatted_isim = isimler_mixer

    soyisimler_mixer = random.choice(soyisimler)
    formatted_soyisim = soyisimler_mixer


    file1 = open("cakmaDATABASE.txt", "a")
    file1.write(f"\nkisi{k} = dbik.Person({tirnak}{formatted_email}{tirnak}, {tirnak}{formatted_password}{tirnak}, {tirnak}{formatted_isim}{tirnak}, {tirnak}{formatted_soyisim}{tirnak})\n")
    file1.close()
    """

    file2 = open("database.py", "a")
    file2.write(f"\nkisi{k} = dbik.Person({tirnak}{formatted_email}{tirnak}, {tirnak}{formatted_password}{tirnak}, {tirnak}{formatted_isim}{tirnak}, {tirnak}{formatted_soyisim}{tirnak})\n")
    file2.close()
"""


emailGenerateBrowser.Browser2("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp")
emailGenerateBrowser.time.sleep(1000)







