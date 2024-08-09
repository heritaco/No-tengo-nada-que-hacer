import sys
import io
import unicodedata

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def comparar_archivos(file1, file2):
    def filtrar_lineas(line):
        return (not line.startswith("Foto del perfil de")                           # No comienza con "Foto del perfil de"
                and not any(c.isupper() for c in line)                              # No contiene mayúsculas
                and ' ' not in line                                                 # No contiene espacios
                and not any(unicodedata.category(c).startswith('S') for c in line)) # No contiene emojis

    # Leer archivos y aplicar filtro, estan por conjuntos
    with open(file1, 'r', encoding='utf-8') as f1:
        lista1 = set(line for line in f1.read().splitlines() if filtrar_lineas(line))
    
    with open(file2, 'r', encoding='utf-8') as f2:
        lista2 = set(line for line in f2.read().splitlines() if filtrar_lineas(line))


    # Comparar listas y encontrar diferencias
    solo_en_file1 = lista1 - lista2
    if solo_en_file1:
        print("Está en", file1, "y no está en", file2 + ":")
        for nombre in solo_en_file1:
            print(nombre)
    else:
        print("No hay nombres en", file1, "que no estén en", file2)


    solo_en_file2 = lista2 - lista1
    if solo_en_file2:
        print("\nEstá en", file2, "y no está en", file1 + ":")
        for nombre in solo_en_file2:
            print(nombre)
    else:
        print("No hay nombres en", file2, "que no estén en", file1)

    # ctrl + abajo del backspace

    # en_ambos = lista1 & lista2

    # if en_ambos:
    #     print("\nEstá en ambos archivos:")
    #     for nombre in en_ambos:
    #         print(nombre)
    # else:
    #     print("No hay nombres que estén en ambos archivos")    


comparar_archivos(r'C:\Users\herie\Downloads\archieve1.txt', 
                  r'C:\Users\herie\Downloads\archieve2.txt')
