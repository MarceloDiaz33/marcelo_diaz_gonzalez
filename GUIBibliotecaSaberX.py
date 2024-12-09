import tkinter as tk
from tkinter import messagebox

# Función para registrar libro 
def registrar_libro():
    titulo = entradaTituloLibro.get()
    autor = entradaAutorLibro.get()
    fecha = entradaFechaPublicacion.get()
    genero = opcionGeneroCategoria.get()
    categorias = []
    if opcion1CategoriaLibro.get():
        categorias.append("Novela")
    if opcion2CategoriaLibro.get():
        categorias.append("Ciencia")
    if opcion3CategoriaLibro.get():
        categorias.append("Historia")
    if opcion4CategoriaLibro.get():
        categorias.append("Otra")
    estado = opcionEstadoDisponibilidad.get()
    copias = entradaIngresoValor.get()
    resumen = textoResumen.get("1.0", "end-1c")
    idioma = escogerIdioma.get() 
    mensaje= f"Libro Registrado con Exito"
    messagebox.showinfo("¡ALERT!", mensaje)


    # Mostrar los detalles en la terminal
    print(f"Título: {titulo}")
    print(f"Autor: {autor}")
    print(f"Año de publicación: {fecha}")
    print(f"Género: {genero}")
    print(f"Categorías: {', '.join(categorias)}")
    print(f"Estado: {estado}")
    print(f"Número de copias: {copias}")
    print(f"Resumen: {resumen}")
    print(f"Idioma: {idioma}")

# Función para limpiar el formulario
def limpiar_formulario():
    entradaTituloLibro.delete(0, 'end')
    entradaAutorLibro.delete(0, 'end')
    entradaFechaPublicacion.delete(0, 'end')
    opcionGeneroCategoria.set(None)
    opcion1CategoriaLibro.set(False)
    opcion2CategoriaLibro.set(False)
    opcion3CategoriaLibro.set(False)
    opcion4CategoriaLibro.set(False)
    opcionEstadoDisponibilidad.set(None)
    entradaIngresoValor.delete(0, 'end')
    textoResumen.delete("1.0", 'end')
    escogerIdioma.set("Escoger Idioma")

ventana = tk.Tk()
ventana.title("Sistema Gestión Biblioteca SaberX")
ventana.geometry("800x600")

tituloFormulario = tk.Label(ventana, text="Formulario de Registro de Libros", font=("Arial", 14, "bold"))
tituloFormulario.pack(pady=10)

formulario = tk.Frame(ventana)
formulario.pack(padx=20, pady=20)

tituloLibro = tk.Label(formulario, text="Título del Libro:")
tituloLibro.grid(row=0, column=0, sticky='e', padx=5, pady=5)
entradaTituloLibro = tk.Entry(formulario, width=40)
entradaTituloLibro.grid(row=0, column=1, padx=5, pady=5)

autorLibro = tk.Label(formulario, text="Autor del Libro:")
autorLibro.grid(row=1, column=0, sticky='e', padx=5, pady=5)
entradaAutorLibro = tk.Entry(formulario, width=40)
entradaAutorLibro.grid(row=1, column=1, padx=5, pady=5)


fechaPublicacion = tk.Label(formulario, text="Año de publicación:")
fechaPublicacion.grid(row=2, column=0, sticky='e', padx=5, pady=5)
entradaFechaPublicacion = tk.Entry(formulario, width=40)
entradaFechaPublicacion.grid(row=2, column=1, padx=5, pady=5)

tituloGeneroCategoria = tk.Label(formulario, text="Género:")
tituloGeneroCategoria.grid(row=3, column=0, sticky='e', padx=5, pady=5)

opcionGeneroCategoria = tk.StringVar()
botonRadio1 = tk.Radiobutton(formulario, text="Ficción", variable=opcionGeneroCategoria, value="Ficción")
botonRadio1.grid(row=3, column=1, sticky='w', padx=5, pady=5)

botonRadio2 = tk.Radiobutton(formulario, text="No Ficción", variable=opcionGeneroCategoria, value="No Ficción")
botonRadio2.grid(row=3, column=2, sticky='w', padx=5, pady=5)

tituloCategoriaLibro = tk.Label(formulario, text="Categoría:")
tituloCategoriaLibro.grid(row=4, column=0, sticky='e', padx=5, pady=5)

opcion1CategoriaLibro = tk.BooleanVar()
opcion2CategoriaLibro = tk.BooleanVar()
opcion3CategoriaLibro = tk.BooleanVar()
opcion4CategoriaLibro = tk.BooleanVar()

checkBoton1 = tk.Checkbutton(formulario, text="Novela", variable=opcion1CategoriaLibro)
checkBoton1.grid(row=4, column=1, sticky='w', padx=5, pady=5)

checkBoton2 = tk.Checkbutton(formulario, text="Ciencia", variable=opcion2CategoriaLibro)
checkBoton2.grid(row=4, column=2, sticky='w', padx=5, pady=5)

checkBoton3 = tk.Checkbutton(formulario, text="Historia", variable=opcion3CategoriaLibro)
checkBoton3.grid(row=4, column=3, sticky='w', padx=5, pady=5)

checkBoton4 = tk.Checkbutton(formulario, text="Otra", variable=opcion4CategoriaLibro)
checkBoton4.grid(row=4, column=4, sticky='w', padx=5, pady=5)


estadoDisponibilidad = tk.Label(formulario, text="Estado:")
estadoDisponibilidad.grid(row=5, column=0, sticky='e', padx=5, pady=5)

opcionEstadoDisponibilidad = tk.StringVar()
botonRadioDisponibilidad1 = tk.Radiobutton(formulario, text="Disponible", variable=opcionEstadoDisponibilidad, value="Disponible")
botonRadioDisponibilidad1.grid(row=5, column=1, sticky='w', padx=5, pady=5)

botonRadioDisponibilidad2 = tk.Radiobutton(formulario, text="Prestado", variable=opcionEstadoDisponibilidad, value="Prestado")
botonRadioDisponibilidad2.grid(row=5, column=2, sticky='w', padx=5, pady=5)


tituloNumCopias = tk.Label(formulario, text="Número de Copias:")
tituloNumCopias.grid(row=6, column=0, sticky='e', padx=5, pady=5)

entradaIngresoValor = tk.Entry(formulario, width=10)
entradaIngresoValor.grid(row=6, column=1, padx=5, pady=5)


tituloResumenLibro = tk.Label(formulario, text="Resumen:")
tituloResumenLibro.grid(row=7, column=0, sticky='e', padx=5, pady=5)

textoResumen = tk.Text(formulario, height=5, width=40)
textoResumen.grid(row=7, column=1, columnspan=2, padx=5, pady=5)


tituloIdiomaLibro = tk.Label(formulario, text="Idioma:")
tituloIdiomaLibro.grid(row=8, column=0, sticky='e', padx=5, pady=5)

escogerIdioma = tk.StringVar(value="Escoger Idioma")
opcionesIdioma = ["Español", "Inglés", "Alemán", "Francés"]

menuIdiomaDesplegable = tk.OptionMenu(formulario, escogerIdioma, *opcionesIdioma)
menuIdiomaDesplegable.grid(row=8, column=1, sticky='w', padx=5, pady=5)

    
botonAccion = tk.Frame(ventana)
botonAccion.pack(pady=20)

ingresarLibro = tk.Button(botonAccion, text="Registrar Libro", command=registrar_libro, width=15)
ingresarLibro.grid(row=0, column=0, padx=20)

borrarFormulario = tk.Button(botonAccion, text="Borrar Formulario", command=limpiar_formulario, width=15)
borrarFormulario.grid(row=0, column=1, padx=20)

ventana.mainloop()
