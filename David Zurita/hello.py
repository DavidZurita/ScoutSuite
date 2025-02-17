import hashlib

print("Hola mundo")

def Sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

print(Sha256("Hola mundo"))
