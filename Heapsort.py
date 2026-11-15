
import tkinter as tk
from tkinter import simpledialog, messagebox

ventana = tk.Tk()
ventana.title("Metodo Heapsort")
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


def heapSort(numeros):
    lista = numeros.copy()
    pasos = []
    cantidad = len(lista)

    def ajustarHeap(n, i):
        mayor = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2

        if izquierda < n and lista[izquierda] > lista[mayor]:
            mayor = izquierda

        if derecha < n and lista[derecha] > lista[mayor]:
            mayor = derecha

        if mayor != i:
            pasos.append(
                "Se intercambian " + str(lista[i]) +
                " y " + str(lista[mayor])
            )

            lista[i], lista[mayor] = lista[mayor], lista[i]
            pasos.append("Lista actual: " + str(lista))

            ajustarHeap(n, mayor)

    pasos.append("Se comienza a construir el monticulo maximo.")

    for i in range(cantidad // 2 - 1, -1, -1):
        ajustarHeap(cantidad, i)

    pasos.append("Monticulo maximo construido: " + str(lista))

    for i in range(cantidad - 1, 0, -1):
        pasos.append(
            "Se coloca el mayor numero " + str(lista[0]) +
            " en su posicion final."
        )

        lista[0], lista[i] = lista[i], lista[0]
        pasos.append("Lista actual: " + str(lista))

        ajustarHeap(i, 0)

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

    resultado, pasos = heapSort(numeros)

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

    mostrarResultado(numeros, "Resultado de Heapsort")


def mostrarEjemplo():
    global indiceEjemplo

    numeros = ejemplos[indiceEjemplo]
    indiceEjemplo = (indiceEjemplo + 1) % len(ejemplos)

    mostrarResultado(numeros, "Ejemplo resuelto de Heapsort")


def menuPrincipal():
    limpiar()

    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(0, weight=1)

    marco = tk.Frame(ventana)
    marco.grid(row=0, column=0)

    tk.Label(
        marco, text="METODO HEAPSORT",
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
