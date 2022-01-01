import pyzipper

with pyzipper.AESZipFile("./Dictionary-attack/downloaded.zip") as my_zip:
    with open("./Dictionary-attack/rockyou.txt", 'r') as dictionary:
        while True:
            password = bytes(dictionary.readline().strip(), 'utf-8')
            try:
                my_zip.extractall(pwd=password)
                print("Password: {}".format(password.decode('utf-8')))
                break

            except RuntimeError:
                pass

            if not dictionary.readline():
                print("Password not found")
                break
