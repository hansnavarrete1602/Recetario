from pathlib import Path, PureWindowsPath
from os import system
import time

home = Path(Path.home(), 'Recetas')


def category_choice():
    while True:
        try:
            system('cls')
            lst_categorias = []
            for root, dirs, files in os.walk(home, topdown=False):
                for name in dirs:
                    lst_categorias.append(os.path.join(root,name))
            print('Selecciona una categoria, escribiendo el numero de inidice que le corresponde')
            for i in range(len(lst_categorias)):
                print(f'{i+1}. {Path(lst_categorias[i]).stem}')
            a = input('¿Que categoria ecoge?: ')
            if a.isdigit():
                return int(a)-1, lst_categorias
            else:
                system('cls')
                print('...Lo siento, sebes de escribir el "numero" del inidice')
                time.sleep(3.5)
                continue
        except KeyboardInterrupt():
            break


def file_choice(a, b):
    while True:
        try:
            system('cls')
            lst_names = []
            guia = Path(b[a])
            for txt in Path(guia).glob("*.txt"):
                lst_names.append(txt.stem)
            if len(lst_names) != 0:
                print(f'Estas son las recetas que existen dentro de la categoria {guia.stem}"')
                print('Seleccione la receta, escribiendo el numero del inidice que le corresponde')
                for i in range(len(lst_names)):
                    print(f'{i+1}. {lst_names[i]}')
                c = input('¿Que receta selecciona?: ')
                if c.isdigit():
                    return b[a], lst_names[int(c)-1]
                else:
                    system('cls')
                    print('...Lo siento, sebes de escribir el "numero" del inidice')
                    time.sleep(3.5)
                    continue
            else:
                print('La categoria esta vacia...')
                time.sleep(3.5)
                return 0, 0
        except KeyboardInterrupt:
            break


def file_open(a, b):
    if a and b != 0:
        b = b + '.txt'
        categoria = Path(a)
        ruta = Path(a, b)
        system('cls')
        print(f'Carpeta raiz: {PureWindowsPath(home)}')
        print(f'Categoria: {categoria.stem}')
        print(f'Receta: {b.replace(".txt", "")}')
        print('\n')
        print(ruta.read_text())
        input()
    else:
        pass


def crear_archivo():
    system('cls')
    name = input('Escribe el nombre de la receta: ')
    system('cls')
    print('Empieza a escribir tu receta en la parte de abajo')
    print('Para terminar con tu escrito, escribe un renglon con solo un simbolo "#"')
    print('de esta manera el software entenderá que tu escrito de la receta ha culminado.')
    print('\n')
    lines = []
    while True:
        receta = input()
        if receta == '#':
            system('cls')
            break
        else:
            lines.append(receta + '\n')
    print('\n...Ahora debes de seleccionar la categoria en la que guardaras tu receta')
    time.sleep(3.5)
    a, b = category_choice()
    print(f'Categoria: {b[a]}')
    print(f'Nombre receta: {name}')
    print(''.join(lines))
    ch = input('\n¿Deseas almacenar la receta? [S/N]: ')
    if ch.lower() == 's':
        n = name + '.txt'
        f = Path(home, b[a], n)
        arch = open(f, 'w')
        arch.writelines(lines)
        arch.close()
        system('cls')
        print(f'receta almacenada en "{b[a]}" con el nombre "{name}"')
        time.sleep(3.5)
        pass
    elif ch.lower() == 'n':
        pass


def eliminar_archivo():
    system('cls')
    print('Ahora debes de seleccionar la categoria donde se encuentra la receta: ')
    a, b = category_choice()
    a, b = file_choice(a, b)
    b = b + '.txt'
    ruta = Path(home, a, b)
    os.remove(ruta)
    system('cls')
    print('Receta eliminada')
    time.sleep(3.5)


def crear_categoria():
    system('cls')
    name = input('Escribe el nombre de la categoria: ')
    ruta = Path(home, name)
    while True:
        if not os.path.exists(ruta):
            system('cls')
            os.mkdir(ruta)
            print(f'...La categoria {name} fue creada!')
            time.sleep(3.5)
            break
        else:
            system('cls')
            print(f'La categoria {name} ya existe...')
            print('...Debes de asignarle otro nombre')
            time.sleep(3.5)
            continue


def eliminar_categoria():
    a, b = category_choice()
    x = b[a]
    system('cls')
    ch = input(f'¿Seguro que quiere eliminar la categoria? [S/N]: ')
    if ch.lower() == 's':
        system('cls')
        shutil.rmtree(x)
        print(f'...categoria eliminada')
        time.sleep(3.5)
        pass
    else:
        system('cls')
        print('Esta bien, volviendo al menu...')
        time.sleep(3.5)
        pass


def menu():
    while True:
        try:
            system('cls')
            print('Carpeta del recetario:')
            print(home)
            print('\n')
            print('...Bienvenido a tu recetario')
            print('Menu:')
            print('1. Leer receta')
            print('2. Crear receta')
            print('3. Crear categoria')
            print('4. Eliminar Receta')
            print('5. Eliminar categoria')
            print('6. Salir del recetario')
            a = input('Seleccione una opcion, escribiendo el numero del indice: ')
            if a.isdigit():
                return int(a)
            else:
                system('cls')
                print('Lo siento, debes de escribir el "numero" del indice')
                time.sleep(3.5)
                continue
        except KeyboardInterrupt():
            break


def recetario():
    while True:
        try:
            c = menu()
            if c == 1:
                print('Ahora debes de seleccionar la categoria que deseas explorar: ')
                a, b = category_choice()
                c, d = file_choice(a, b)
                file_open(c, d)
                continue
            elif c == 2:
                crear_archivo()
                continue
            elif c == 3:
                crear_categoria()
                continue
            elif c == 4:
                eliminar_archivo()
                continue
            elif c == 5:
                eliminar_categoria()
                continue
            elif c == 6:
                system('cls')
                break
            else:
                system('cls')
                print(f'Lo siento "{c}", no es una opcion valida')
                print('selecciona una opcion dentro del menu')
                time.sleep(3.5)
                continue
        except KeyboardInterrupt:
            break


recetario()
