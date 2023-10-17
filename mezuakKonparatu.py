import hashlib

ruta = "/home/jon/LaboISSKS/mezua.txt"
with open(ruta, 'rb') as archivo:
	contenido = archivo.read()
hash_obj = hashlib.md5()
hash_obj.update(contenido)
hash_emaitza = hash_obj.hexdigest()
if hash_emaitza == "89362fb28ce0ddf3d1e90e484150c608":
	print("Mezua berdina da")
else:
	print("Mezua ez da berdina")
		
