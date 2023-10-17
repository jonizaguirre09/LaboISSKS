import hashlib
nombre_archivo = "mezua.txt"

def calcular_md5(archivo):
	md5_hash = hashlib.md5()
	with open(archivo, 'rb') as f:
		contenido = f.read()
	md5_hash.update(contenido)
	return md5_hash.hexdigest()

hash_md5 = calcular_md5(nombre_archivo)

print(hash_md5)
