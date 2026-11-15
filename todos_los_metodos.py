
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

ventana = tk.Tk()
ventana.title("Metodos de Ordenamiento")
ventana.minsize(650, 450)

try:
    ventana.state("zoomed")
except tk.TclError:
    ventana.geometry(
        str(ventana.winfo_screenwidth()) + "x" +
        str(ventana.winfo_screenheight() - 80) + "+0+0"
    )

metodos = ["ShellSort", "Quicksort", "Heapsort", "Radix Sort"]

ejemplos = {
    "ShellSort": [
        [35, 12, 48, 7, 23, 19],
        [50, 10, 40, 20, 30, 5],
        [18, 45, 9, 32, 14, 27]
    ],
    "Quicksort": [
        [42, 15, 8, 23, 36, 11],
        [60, 25, 10, 45, 5, 30],
        [19, 33, 7, 28, 14, 40]
    ],
    "Heapsort": [
        [31, 16, 44, 9, 27, 12],
        [55, 20, 35, 10, 45, 5],
        [22, 8, 39, 17, 29, 13]
    ],
    "Radix Sort": [
        [170, 45, 75, 90, 802, 24],
        [329, 457, 657, 839, 436, 720],
        [64, 12, 305, 8, 91, 27]
    ]
}

indices = {
    "ShellSort": 0,
    "Quicksort": 0,
    "Heapsort": 0,
    "Radix Sort": 0
}


def limpiar():
    for widget in ventana.winfo_children():
        widget.destroy()


def shellSort(numeros):
    lista = numeros.copy()
    pasos = []
    salto = len(lista) // 2

    while salto > 0:
        pasos.append("Se utiliza un salto de: " + str(salto))

        for i in range(salto, len(lista)):
            temporal = lista[i]
            j = i

            pasos.append("Se toma el numero " + str(temporal))

            while j >= salto and lista[j - salto] > temporal:
                pasos.append(
                    "Se mueve " + str(lista[j - salto]) +
                    " hacia la derecha."
                )
                lista[j] = lista[j - salto]
                j -= salto

            lista[j] = temporal
            pasos.append("Lista actual: " + str(lista))

        salto //= 2

    pasos.append("El ordenamiento ha terminado.")
    return lista, pasos


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


def radixSort(numeros):
    lista = numeros.copy()
    pasos = []

    if any(numero < 0 for numero in lista):
        raise ValueError("Radix Sort necesita numeros no negativos.")

    if not lista:
        return lista, pasos

    mayor = max(lista)
    posicion = 1

    while mayor // posicion > 0:
        cubetas = [[] for _ in range(10)]

        pasos.append(
            "Se revisan los digitos de la posicion " + str(posicion) + "."
        )

        for numero in lista:
            digito = (numero // posicion) % 10
            cubetas[digito].append(numero)

            pasos.append(
                "El numero " + str(numero) +
                " se coloca en la cubeta " + str(digito) + "."
            )

        lista = []

        for i in range(10):
            if cubetas[i]:
                pasos.append(
                    "Contenido de la cubeta " + str(i) +
                    ": " + str(cubetas[i])
                )
                lista.extend(cubetas[i])

        pasos.append("Lista despues de esta posicion: " + str(lista))
        posicion *= 10

    pasos.append("El ordenamiento ha terminado.")
    return lista, pasos


def ejecutarMetodo(metodo, numeros):
    if metodo == "ShellSort":
        return shellSort(numeros)

    elif metodo == "Quicksort":
        return quickSort(numeros)

    elif metodo == "Heapsort":
        return heapSort(numeros)

    elif metodo == "Radix Sort":
        return radixSort(numeros)


def mostrarResultado(metodo, numeros, titulo):
    limpiar()

    ventana.rowconfigure(0, weight=0)
    ventana.rowconfigure(1, weight=1)
    ventana.rowconfigure(2, weight=0)
    ventana.columnconfigure(0, weight=1)

    tk.Label(
        ventana,
        text=titulo + " - " + metodo,
        font=("Arial", 20, "bold")
    ).grid(row=0, column=0, pady=12)

    try:
        resultado, pasos = ejecutarMetodo(metodo, numeros)
    except ValueError as error:
        messagebox.showerror("Error", str(error))
        menuPrincipal()
        return

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

    texto.insert("end", "Metodo seleccionado: " + metodo + "\n")
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
    metodo = variableMetodo.get()

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

        if metodo == "Radix Sort" and numero < 0:
            messagebox.showerror(
                "Numero no valido",
                "Radix Sort solo acepta numeros enteros no negativos."
            )
            return

        numeros.append(numero)

    mostrarResultado(metodo, numeros, "Resultado del ejercicio")


def mostrarEjemplo():
    metodo = variableMetodo.get()

    indice = indices[metodo]
    numeros = ejemplos[metodo][indice]

    indices[metodo] = (indice + 1) % len(ejemplos[metodo])

    mostrarResultado(metodo, numeros, "Ejemplo resuelto")


def menuPrincipal():
    global variableMetodo

    limpiar()

    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(0, weight=1)

    marco = tk.Frame(ventana)
    marco.grid(row=0, column=0)

    tk.Label(
        marco,
        text="METODOS DE ORDENAMIENTO",
        font=("Arial", 24, "bold")
    ).pack(pady=20)

    tk.Label(
        marco,
        text="Selecciona el metodo que deseas utilizar:",
        font=("Arial", 13)
    ).pack(pady=8)

    variableMetodo = tk.StringVar(value="ShellSort")

    listaMetodos = ttk.Combobox(
        marco,
        textvariable=variableMetodo,
        values=metodos,
        state="readonly",
        width=30,
        font=("Arial", 12)
    )
    listaMetodos.pack(pady=12)

    tk.Button(
        marco,
        text="1. Resolver mi ejercicio",
        command=resolverEjercicio,
        width=32, height=2
    ).pack(pady=10)

    tk.Button(
        marco,
        text="2. Mostrar ejemplo resuelto",
        command=mostrarEjemplo,
        width=32, height=2
    ).pack(pady=10)

    tk.Button(
        marco,
        text="3. Salir",
        command=ventana.destroy,
        width=32, height=2
    ).pack(pady=10)


menuPrincipal()
ventana.mainloop()
