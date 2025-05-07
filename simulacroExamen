# Simulacro examen riwi

import re

listaLibros = []

def agregarLibro(titulo, autor, copias, genero):
    libro = {
        "titulo" : titulo,
        "autor"  : autor,
        "copias" : copias,
        "genero" : genero
    }
    listaLibros.append(libro)


def buscarLibro():
    buscar = input("Enter the title of the book to search:")

    for libro in listaLibros:
        if libro["titulo"] == buscar:
            print("Book found \n")
            print(libro)
    else:
        print("Book not found")

def registrarPrestamo():

    registrar = input("Enter the book you want to borrow:\n")

    for libro in listaLibros:
        if libro["titulo"] == registrar:
            print("Making loan...")
            if libro.get("copias") > 0:
                print("Loan made successfully")
                libro["copias"] -= 1
            else:
                print("We do not have copies of this book at the moment.")
    else:
            print("Book not found")

def devolverLibro():
    devolver = input("Enter the book you want to return: \n")

    for libro in listaLibros:
        if libro["titulo"] == devolver:
            libro["copias"] += 1
            print("Correct return, thank you very much.")

def eliminarLibro():
    for libro in listaLibros:
        if libro["copias"] == 0:
            listaLibros.pop(libro)

def listarLibro():
    opcion = input("Enter an option to search for books by genre: \n"
                   "1: Fiction\n"
                   "2: Non-Fiction\n"
                   "3: Science\n"
                   "4: Biography\n"
                   "5: Children")

    match opcion:
        case "1":
            opcion = "Fiction"
        case "2":
            opcion = "Non-Fiction"
        case "3":
            opcion = "Science"
        case "4":
            opcion = "Biography"
        case "5":
            opcion =  "Children"

    for libro in listaLibros:
        if libro[genero] == opcion:
            print(libro["titulo"])
        else:
            print("invalid option")


def verInventario():
    print(f" The number of books in the library are: {len(listaLibros)}")

    copiasTotales = 0

    for libro in listaLibros:
        copiasTotales = copiasTotales + libro.get["copias"]

    print(f"The total copies in existence of the library are: {copiasTotales} ")

opcion = input(print("Welcome to the Riwi Library, please enter an option to get started: \n"
      "1: Add book\n"
      "2: Search book\n"
      "3: Loan book\n"
      "4: Return book\n"
      "5 Search book by genre\n"
      "6: View inventory\n"))

match opcion:
    case "1":

        while True:
                titulo = input("Enter the name of the book you want to add:1")
                if re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚñÑ ]+", titulo):
                    break
                else:
                    print("Please enter a valid book name")

        while True:
            autor = input("Enter the author of the book")
            if re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚñÑ ]+", autor):
                break                                                   
            else:
                print("Invalid author name")

        while True:
            try:
                copias = int(input("Enter the number of copies available: "))
                break
            except ValueError:
                print("Enter an integer value")
        while True:
            genero = input("Enter the genre of the book from the following options: 'Fiction', 'Non-Fiction', 'Science', 'Biography', 'Children'")
            if re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚñÑ ]+", genero):
                break
            else:
                print("Please enter a correct option")
        agregarLibro(titulo, autor, copias, genero)

    case "2":
        buscarLibro()

    case "3":
        registrarPrestamo()

    case "4":
        devolverLibro()

    case "5":
        listarLibro()

    case "6":
        verInventario()






