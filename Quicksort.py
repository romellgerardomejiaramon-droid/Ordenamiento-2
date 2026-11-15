
import tkinter as tk
from tkinter import simpledialog, messagebox

ventana = tk.Tk()
ventana.title("Metodo Quicksort")
ventana.minsize(650, 450)

try:
    ventana.state("zoomed")
except tk.TclError:
    ventana.geometry(
        str(ventana.winfo_screenwidth()) + "x" +
        str(ventana.winfo_screenheight() - 80) + "+0+0"
    )

ejemplos = [
    [35, 12, 48, 7, 23, 19],
    [50, 10, 40, 20, 30, 5],
    [18, 45, 9, 32, 14, 27]
]
indiceEjemplo = 0


def limpiar():
    for widget in ventana.winfo_children():
        widget.destroy()


def quickSort(numeros):
    lista = numeros.copy()
    pasos = []

    def ordenar(inicio, fin):
        if inicio >= fin:
            return

        pivote = lista[(inicio + fin) // 2]
        pasos.append("Se elige como pivote el numero " + str(pivote))

        izquierda = inicio
        derecha = fin

        while izquierda <= derecha:
            while lista[izquierda] < pivote:
                izquierda += 1

            while lista[derecha] > pivote:
                derecha -= 1

            if izquierda <= derecha:
                pasos.append(
                    "Se intercambian " + str(lista[izquierda]) +
                    " y " + str(lista[derecha])
                )

                lista[izquierda], lista[derecha] = (
                    lista[derecha], lista[izquierda]
                )

                pasos.append("Lista actual: " + str(lista))

                izquierda += 1
                derecha -= 1

        if inicio < derecha:
            pasos.append("Se ordena la parte izquierda.")
            ordenar(inicio, derecha)

        if izquierda < fin:
            pasos.append("Se ordena la parte derecha.")
            ordenar(izquierda, fin)

    if lista:
        ordenar(0, len(lista) - 1)

    pasos.append("El ordenamiento ha terminado.")
    return lista, pasos


def mostrarResultado(numeros, titulo):
    limpiar()

    ventana.rowconfigure(0, weight=0)
    ventana.rowconfigure(1, weight=1)
    ventana.rowconfigure(2, weight=0)
    ventana.columnconfigure(0, weight=1)

    tk.Label(
        ventana, text=titulo,
        font=("Arial", 20, "bold")
    ).grid(row=0, column=0, pady=12)

    resultado, pasos = quickSort(numeros)

    marcoTexto = tk.Frame(ventana)
    marcoTexto.grid(
        row=1, column=0, sticky="nsew",
        padx=20, pady=5
    )
    marcoTexto.rowconfigure(0, weight=1)
    marcoTexto.columnconfigure(0, weight=1)

    texto = tk.Text(
        marcoTexto, wrap="word",
        font=("Arial", 12)
    )
    texto.grid(row=0, column=0, sticky="nsew")

    barraVertical = tk.Scrollbar(
        marcoTexto, orient="vertical",
        command=texto.yview
    )
    barraVertical.grid(row=0, column=1, sticky="ns")

    barraHorizontal = tk.Scrollbar(
        marcoTexto, orient="horizontal",
        command=texto.xview
    )
    barraHorizontal.grid(row=1, column=0, sticky="ew")

    texto.config(
        yscrollcommand=barraVertical.set,
        xscrollcommand=barraHorizontal.set
    )

    texto.insert("end", "Numeros ingresados: " + str(numeros) + "\n\n")
    texto.insert("end", "PROCEDIMIENTO PASO A PASO\n\n")

    for paso in pasos:
        texto.insert("end", paso + "\n")

    texto.insert("end", "\nRESULTADO FINAL\n")
    texto.insert("end", str(resultado))
    texto.config(state="disabled")

    marcoBotones = tk.Frame(ventana)
    marcoBotones.grid(row=2, column=0, pady=12)

    tk.Button(
        marcoBotones,
        text="Volver al menu principal",
        command=menuPrincipal,
        width=25, height=2
    ).pack(side="left", padx=10)

    tk.Button(
        marcoBotones,
        text="Salir",
        command=ventana.destroy,
        width=15, height=2
    ).pack(side="left", padx=10)


def resolverEjercicio():
    cantidad = simpledialog.askinteger(
        "Cantidad de numeros",
        "Cuantos numeros deseas ordenar?",
        parent=ventana,
        minvalue=1,
        maxvalue=100
    )

    if cantidad is None:
        return

    numeros = []

    for i in range(cantidad):
        numero = simpledialog.askinteger(
            "Ingresar numero",
            "Ingresa el numero " + str(i + 1) + ":",
            parent=ventana
        )

        if numero is None:
            return

        numeros.append(numero)

    mostrarResultado(numeros, "Resultado de Quicksort")


def mostrarEjemplo():
    global indiceEjemplo

    numeros = ejemplos[indiceEjemplo]
    indiceEjemplo = (indiceEjemplo + 1) % len(ejemplos)

    mostrarResultado(numeros, "Ejemplo resuelto de Quicksort")


def menuPrincipal():
    limpiar()

    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(0, weight=1)

    marco = tk.Frame(ventana)
    marco.grid(row=0, column=0)

    tk.Label(
        marco, text="METODO QUICKSORT",
        font=("Arial", 24, "bold")
    ).pack(pady=25)

    tk.Button(
        marco, text="1. Resolver mi ejercicio",
        command=resolverEjercicio,
        width=32, height=2
    ).pack(pady=12)

    tk.Button(
        marco, text="2. Mostrar ejemplo resuelto",
        command=mostrarEjemplo,
        width=32, height=2
    ).pack(pady=12)

    tk.Button(
        marco, text="3. Salir",
        command=ventana.destroy,
        width=32, height=2
    ).pack(pady=12)


menuPrincipal()
ventana.mainloop()
