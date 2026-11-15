# Ordenamiento-2

# Métodos de Ordenamiento en Python

## Descripción del proyecto

Este proyecto consiste en la implementación de cuatro métodos de ordenamiento en el lenguaje de programación Python: ShellSort, Quicksort, Heapsort y Radix Sort.

Cada método cuenta con un programa independiente que permite ingresar una cantidad de números, ordenarlos y visualizar el procedimiento que realiza el algoritmo paso a paso. También incluye una opción para mostrar ejemplos resueltos y otra para salir del programa.

Además, se desarrolló un programa general que reúne los cuatro métodos y permite seleccionar cuál se desea utilizar desde un mismo menú.

Los programas utilizan la biblioteca Tkinter para crear una interfaz gráfica que facilita la interacción con el usuario.

---

# 1. Programa ShellSort

## 1.1 Funcionamiento interno

El programa ShellSort utiliza el método de ordenamiento ShellSort, el cual organiza los números mediante comparaciones e intercambios entre elementos que se encuentran separados por una determinada distancia.

Su funcionamiento comienza creando una copia de los números ingresados para trabajar con ellos sin modificar la lista original.

Posteriormente, calcula un salto inicial que corresponde a la mitad de la cantidad de elementos. Utilizando este salto, compara los números que se encuentran separados por esa distancia y realiza movimientos cuando encuentra elementos que necesitan cambiar de posición.

Después de cada recorrido, el salto se reduce a la mitad. Este proceso continúa hasta que el salto llega a cero y todos los elementos quedan ordenados.

### Funciones principales

- **shellSort(numeros):** recibe los números, realiza el procedimiento de ordenamiento y almacena los pasos que se van ejecutando.
- **mostrarResultado(numeros, titulo):** presenta los números ingresados, el procedimiento paso a paso y el resultado final.
- **resolverEjercicio():** solicita al usuario la cantidad de números y posteriormente pide cada uno para realizar el ordenamiento.
- **mostrarEjemplo():** presenta un ejercicio de ejemplo con su procedimiento. Los ejemplos cambian cada vez que se selecciona esta opción.
- **menuPrincipal():** muestra las opciones disponibles para interactuar con el programa.
- **limpiar():** elimina los elementos de la interfaz anterior para mostrar la siguiente pantalla.

## 1.2 Funcionamiento externo

Para ejecutar el programa, se abre la terminal en la carpeta donde se encuentra el archivo y se escribe:

```bash
python ShellSort.py
```

Al iniciar, aparece una ventana con el título **METODO SHELLSORT** y tres opciones principales:

**Opción 1. Resolver mi ejercicio**

Al seleccionar esta opción, el programa solicita la cantidad de números que se desean ordenar. Después pide ingresar cada número individualmente.

Una vez capturados los datos, muestra los números originales, el procedimiento que realiza ShellSort y la lista ordenada al finalizar.

**Opción 2. Mostrar ejemplo resuelto**

Esta opción presenta un conjunto de números previamente establecido. El programa muestra cómo se van realizando las comparaciones y movimientos hasta obtener el resultado ordenado.

Cada vez que se vuelve a seleccionar esta opción, se presenta un ejemplo diferente.

**Opción 3. Salir**

Cierra la ventana y finaliza la ejecución del programa.

Después de resolver un ejercicio o visualizar un ejemplo, aparecen dos botones adicionales:

- **Volver al menu principal:** permite regresar a las tres opciones iniciales.
- **Salir:** permite cerrar el programa directamente.

---

# 2. Programa Quicksort

## 2.1 Funcionamiento interno

El programa Quicksort utiliza un método de ordenamiento basado en la división de los elementos mediante un número llamado pivote.

Primero, el programa recibe los números y crea una copia de la lista original. Después selecciona un elemento central como pivote.

A partir de este elemento, utiliza dos posiciones para recorrer la lista: una comienza desde la izquierda y otra desde la derecha.

La posición izquierda busca números mayores o iguales al pivote, mientras que la posición derecha busca números menores o iguales. Cuando se encuentran elementos que deben intercambiarse, el programa realiza el movimiento correspondiente.

Este procedimiento permite dividir la lista en partes más pequeñas. Posteriormente, Quicksort vuelve a aplicar el mismo proceso sobre las partes izquierda y derecha hasta conseguir que todos los números queden ordenados.

### Funciones principales

- **quickSort(numeros):** recibe la lista de números y realiza el ordenamiento utilizando el pivote y las divisiones de la lista.
- **ordenar(inicio, fin):** función interna que realiza las particiones y las llamadas recursivas para ordenar las diferentes partes.
- **mostrarResultado(numeros, titulo):** muestra los números originales, las operaciones realizadas y el resultado final.
- **resolverEjercicio():** solicita la cantidad de números y sus respectivos valores.
- **mostrarEjemplo():** presenta ejemplos previamente establecidos y muestra su procedimiento.
- **menuPrincipal():** permite elegir entre resolver un ejercicio, mostrar un ejemplo o salir.
- **limpiar():** elimina los elementos anteriores de la interfaz para presentar una nueva pantalla.

## 2.2 Funcionamiento externo

Para ejecutar el programa desde la terminal, se utiliza el siguiente comando:

```bash
python Quicksort.py
```

Al abrirse la ventana aparece el título **METODO QUICKSORT**, acompañado de tres opciones.

**Opción 1. Resolver mi ejercicio**

Solicita la cantidad de números que se desean ordenar y después pide ingresar cada valor.

Al terminar de ingresar los datos, el programa selecciona el pivote y muestra los intercambios y las divisiones que realiza Quicksort hasta obtener la lista ordenada.

**Opción 2. Mostrar ejemplo resuelto**

Muestra un ejercicio con números previamente definidos y explica cómo trabaja el algoritmo desde la selección del pivote hasta el resultado final.

Al volver a seleccionar esta opción, se muestra otro ejemplo.

**Opción 3. Salir**

Finaliza la ejecución y cierra la ventana.

Después de mostrar el procedimiento y el resultado, se encuentran los botones para regresar al menú principal o salir del programa.

---

# 3. Programa Heapsort

## 3.1 Funcionamiento interno

El programa Heapsort utiliza una estructura llamada montículo máximo o Max Heap para organizar los números.

Su funcionamiento comienza recibiendo los números y creando una copia de la lista original.

Después construye un montículo máximo, en el cual el elemento de mayor valor se encuentra en la primera posición. Para conseguirlo, compara los elementos y realiza intercambios cuando es necesario.

Una vez construido el montículo, el programa toma el número más grande y lo coloca en la última posición disponible de la lista.

Posteriormente, reduce el tamaño de la parte que todavía necesita ordenarse y vuelve a ajustar el montículo para que el siguiente número mayor quede en la primera posición.

Este proceso se repite hasta que todos los números quedan organizados de menor a mayor.

### Funciones principales

- **heapSort(numeros):** recibe los números, construye el montículo máximo y realiza el ordenamiento.
- **ajustarHeap(n, i):** función interna que compara un elemento con sus hijos y realiza los intercambios necesarios para mantener la estructura del montículo máximo.
- **mostrarResultado(numeros, titulo):** presenta los números ingresados, la construcción del montículo, los intercambios y el resultado final.
- **resolverEjercicio():** solicita la cantidad de números y sus valores para ejecutar Heapsort.
- **mostrarEjemplo():** muestra ejercicios previamente definidos para observar el procedimiento del algoritmo.
- **menuPrincipal():** presenta las opciones principales del programa.
- **limpiar():** elimina los elementos de la interfaz anterior.

## 3.2 Funcionamiento externo

Para iniciar el programa desde la terminal, se utiliza:

```bash
python Heapsort.py
```

Al ejecutarlo, aparece una ventana con el título **METODO HEAPSORT** y tres opciones.

**Opción 1. Resolver mi ejercicio**

El programa solicita la cantidad de números y después pide ingresar cada uno.

Cuando se terminan de capturar los datos, comienza a construir el montículo máximo. Posteriormente muestra cómo se intercambian los elementos y cómo se coloca cada número mayor en su posición correspondiente.

Finalmente, presenta la lista ordenada.

**Opción 2. Mostrar ejemplo resuelto**

Presenta una lista de números previamente establecida y muestra cómo se construye el montículo máximo y cómo se van colocando los elementos hasta obtener el resultado.

Los ejemplos cambian al volver a seleccionar esta opción.

**Opción 3. Salir**

Cierra la ventana y termina el programa.

Después de mostrar el resultado, se puede regresar al menú principal o cerrar el programa utilizando los botones disponibles en la parte inferior.

---

# 4. Programa Radix Sort

## 4.1 Funcionamiento interno

El programa Radix Sort utiliza un método de ordenamiento que organiza los números tomando en cuenta sus dígitos, comenzando por las unidades, después las decenas, las centenas y así sucesivamente.

Primero recibe los números y crea una copia de la lista original. Después identifica cuál es el número con mayor cantidad de dígitos para determinar cuántas posiciones necesita revisar.

El programa utiliza diez cubetas, identificadas del 0 al 9. En cada recorrido obtiene el dígito correspondiente a la posición que está trabajando y coloca el número en la cubeta que corresponde a ese dígito.

Una vez distribuidos todos los números, los reúne nuevamente siguiendo el orden de las cubetas.

Después repite el procedimiento con la siguiente posición decimal hasta terminar de revisar todos los dígitos necesarios.

Al finalizar, obtiene una lista ordenada de menor a mayor.

Este programa trabaja con números enteros no negativos.

### Funciones principales

- **radixSort(numeros):** recibe los números, identifica el valor mayor, distribuye los elementos en las cubetas y realiza los recorridos necesarios para ordenarlos.
- **mostrarResultado(numeros, titulo):** muestra los números originales, la distribución en las cubetas y el resultado final.
- **resolverEjercicio():** solicita la cantidad de números y sus valores. También verifica que no se ingresen números negativos.
- **mostrarEjemplo():** presenta ejemplos previamente establecidos para observar cómo trabaja el algoritmo.
- **menuPrincipal():** muestra las opciones principales del programa.
- **limpiar():** elimina los elementos anteriores de la interfaz.

## 4.2 Funcionamiento externo

Para ejecutar el programa desde la terminal, se utiliza:

```bash
python RadixSort.py
```

Al iniciar, aparece una ventana con el título **METODO RADIX SORT** y tres opciones.

**Opción 1. Resolver mi ejercicio**

El programa solicita la cantidad de números que se desean ordenar y después pide ingresar cada valor.

Cuando se termina de capturar la información, comienza a revisar los dígitos de cada número.

En pantalla se muestra en qué cubeta se coloca cada elemento y cómo se vuelve a formar la lista después de cada recorrido.

Si se ingresa un número negativo, aparece un mensaje indicando que Radix Sort solamente acepta números enteros no negativos.

**Opción 2. Mostrar ejemplo resuelto**

Presenta una lista de números previamente establecida y muestra cómo se distribuyen en las cubetas durante las unidades, decenas, centenas y demás posiciones necesarias.

Cada vez que se selecciona nuevamente esta opción, aparece otro ejemplo.

**Opción 3. Salir**

Cierra la ventana y finaliza la ejecución.

Después de mostrar el procedimiento y el resultado, el usuario puede regresar al menú principal o salir del programa.

---

# 5. Programa general: Todos_los_metodos.py

## 5.1 Funcionamiento interno

Este programa reúne los cuatro métodos de ordenamiento desarrollados anteriormente: ShellSort, Quicksort, Heapsort y Radix Sort.

Su objetivo es permitir que el usuario seleccione cualquiera de los algoritmos desde una misma interfaz gráfica, sin tener que ejecutar cada programa individualmente.

Internamente contiene las funciones de los cuatro métodos de ordenamiento. Cada uno conserva su propio procedimiento y genera los pasos necesarios para mostrar cómo organiza los números.

El programa utiliza una variable para guardar el método seleccionado y un conjunto de funciones para ejecutar el algoritmo correspondiente.

Cuando el usuario selecciona un método y elige resolver un ejercicio, los números ingresados se envían a la función correspondiente. Esta realiza el ordenamiento y devuelve tanto la lista ordenada como los pasos del procedimiento.

También cuenta con ejemplos independientes para cada algoritmo, de manera que al seleccionar la opción de ejemplo se muestran los números correspondientes al método elegido.

### Funciones principales

- **shellSort(numeros):** realiza el ordenamiento utilizando saltos que se van reduciendo progresivamente.
- **quickSort(numeros):** organiza los elementos mediante un pivote y divisiones recursivas.
- **heapSort(numeros):** construye un montículo máximo y coloca los elementos en sus posiciones correspondientes.
- **radixSort(numeros):** distribuye los números en cubetas según sus dígitos.
- **ejecutarMetodo(metodo, numeros):** identifica el método seleccionado y ejecuta la función correspondiente.
- **mostrarResultado(metodo, numeros, titulo):** presenta el algoritmo seleccionado, los números ingresados, el procedimiento y el resultado final.
- **resolverEjercicio():** solicita la cantidad de números y sus valores para enviarlos al método seleccionado.
- **mostrarEjemplo():** muestra un ejemplo del algoritmo seleccionado.
- **menuPrincipal():** presenta el selector de métodos y las opciones disponibles.
- **limpiar():** elimina los elementos anteriores de la interfaz para mostrar una nueva pantalla.

## 5.2 Funcionamiento externo

Para ejecutar el programa general desde la terminal, se utiliza:

```bash
python Todos_los_metodos.py
```

Al iniciar aparece una ventana con el título **METODOS DE ORDENAMIENTO**.

En esta pantalla se encuentra un selector desplegable que permite elegir uno de los cuatro métodos disponibles:

- ShellSort
- Quicksort
- Heapsort
- Radix Sort

Después de seleccionar el algoritmo, se presentan tres opciones.

**Opción 1. Resolver mi ejercicio**

Al seleccionar esta opción, el programa solicita la cantidad de números que se desean ordenar y después pide ingresar cada valor.

Una vez capturados los datos, ejecuta el algoritmo seleccionado y muestra el procedimiento paso a paso, junto con el resultado final.

Si se selecciona Radix Sort, el programa verifica que los números ingresados sean no negativos.

**Opción 2. Mostrar ejemplo resuelto**

Esta opción presenta un ejemplo correspondiente al método que se encuentra seleccionado.

El programa muestra los números iniciales, el procedimiento que realiza el algoritmo y el resultado ordenado.

Cada método cuenta con sus propios ejemplos, por lo que al cambiar el algoritmo también cambia el ejercicio que se presenta.

**Opción 3. Salir**

Cierra la ventana y finaliza la ejecución del programa.

Después de resolver un ejercicio o mostrar un ejemplo, aparecen los botones para regresar al menú principal o salir directamente.

---

# 6. Interfaz gráfica y elementos generales

Los cinco programas utilizan Tkinter para construir sus interfaces gráficas.

La interfaz permite que el usuario pueda trabajar con los algoritmos mediante botones, ventanas de entrada y áreas donde se muestra el procedimiento.

Entre los elementos generales se encuentran:

- **Ventana principal:** contiene el menú y las pantallas de resultados.
- **Botones:** permiten seleccionar las opciones disponibles.
- **Ventanas de entrada:** solicitan la cantidad de números y cada uno de sus valores.
- **Área de resultados:** muestra los números originales, el procedimiento y la lista ordenada.
- **Barras de desplazamiento:** permiten consultar el procedimiento completo cuando ocupa más espacio del disponible.
- **Botón de regreso:** permite volver al menú principal sin cerrar el programa.

# 7. Conclusión

El desarrollo de este proyecto permitió implementar y comprender cuatro métodos diferentes de ordenamiento mediante Python: ShellSort, Quicksort, Heapsort y Radix Sort.

Aunque todos tienen el mismo objetivo de organizar números de menor a mayor, cada uno utiliza un procedimiento diferente para conseguirlo. ShellSort trabaja mediante saltos, Quicksort utiliza un pivote, Heapsort emplea un montículo máximo y Radix Sort distribuye los números tomando en cuenta sus dígitos.

La creación de programas independientes permitió observar el funcionamiento de cada algoritmo de manera individual. Posteriormente, se integraron los cuatro métodos en un solo programa para facilitar su selección y utilización.

También se implementó una interfaz gráfica con Tkinter que permite ingresar datos, visualizar ejemplos y observar los procedimientos paso a paso. De esta manera, el proyecto no solamente realiza el ordenamiento, sino que también permite comprender cómo trabaja cada método.

