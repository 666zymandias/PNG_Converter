from PIL import Image
import sys
from pathlib import Path
import os

def info_programa():
    print()
    print("Conversor de imagen en formato .webp a png por consola")
    print("Creado por Jaider Felipe Santos Garzon")
    print("Version 1.0")
    print()

def get_file_route():
    try:
        file_route = sys.argv[1] + ".webp"
    except IndexError:
        file_route = input("Introduce la ruta absoluta a tu archivo: ")
    
    path = Path(file_route)
    input_file = path.with_suffix(".webp")
    return input_file

def print_img_info(img):    
    print()
    print(f"Formato: {img.format}")
    print(f"Tamaño: {img.size}")
    print(f"Modo: {img.mode}")

    if img.info.get("lossless"):
        print("Tipo de compresion: Lossy")
    else:
        print("Tipo de compresion: Lossy")
    print()

def convert_file(img, file_route):
    try:
        path = Path(file_route)
        output_file = path.with_suffix(".png")

        img.save(output_file, "PNG")

        os.remove(path)

        print("Imagen guardada correctamente.")

    except (FileNotFoundError, PermissionError, OSError, ValueError) as e:
        print(f"No se pudo guardar la imagen: {e}")


def main():
    try:
        #Abrir archivo
        file_route = get_file_route()
        img = Image.open(file_route)
        print("Imagen abierta correctamente.")
        
        #Mostrar información archivo
        print_img_info(img)
        
        #Convertir de webp a png
        convert = input("Deseas transfomar este archivo de webp a png? [Y] Si [N] No: ")
        if convert == 'Y' or convert == 'y':
            convert_file(img, file_route)

        print("Adios!")
        
    except FileNotFoundError:
        print("El archivo de imagen no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    except KeyboardInterrupt:
        print()
    print()
    

info_programa()
main()