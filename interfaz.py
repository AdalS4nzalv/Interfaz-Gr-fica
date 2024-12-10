import tkinter as tk
from tkinter import ttk
from cuentas import DispositivosAlmacenamiento

def convertirMbAGb():
    try:
        tamanoMB = float(input_conversion.get())
        if tamanoMB < 0:  
            raise ValueError("Introduce un valor positivo.")
        
        
        etiqueta_error_MB1.config(text="")
        etiqueta_error_MB2.config(text="")
        
        # Crear un objeto de la clase
        conversionUnidades = DispositivosAlmacenamiento()
        tamanoGB = conversionUnidades.convertirTamanoMBAGB(tamanoMB)
        tamanoTB = conversionUnidades.convertirTamanoGBATB(tamanoGB)
        dispositivosNecesarios = conversionUnidades.calcularDispositivosNecesarios(tamanoGB)

        etiqueta_tamanoGB.config(text=f"El tamaño en GB es: {tamanoGB:.2f}")
        etiqueta_tamanoTB.config(text=f"El tamaño en TB es: {tamanoTB:.6f}")
        etiqueta_dispositivosAlmacenamiento.config(
            text=f"Memorias USB de 4 GB necesarias: {int(dispositivosNecesarios)}")
    except ValueError as ve:
        if "could not convert" in str(ve):
            etiqueta_error_MB1.config(text="Introduce un valor numérico.")
        else:
            etiqueta_error_MB2.config(text=str(ve))

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Conversión de unidades de almacenamiento")
ventana.config(width=500, height=300)

# Etiqueta para la entrada
etiqueta_MB = ttk.Label(text="Introduce el tamaño del archivo en MB:")
etiqueta_MB.place(x=10, y=10)

# Entrada de texto
input_conversion = ttk.Entry()
input_conversion.place(x=220, y=10, width=80)

# Etiquetas para errores 
etiqueta_error_MB1 = ttk.Label(text="")
etiqueta_error_MB1.place(x=300, y=10)
etiqueta_error_MB2 = ttk.Label(text="")
etiqueta_error_MB2.place(x=300, y=30)

# Botón de conversión
boton_convertir = ttk.Button(text="Convertir", command=convertirMbAGb)
boton_convertir.place(x=100, y=100)

# Etiquetas para resultados
etiqueta_tamanoGB = ttk.Label(text="El tamaño en GB es: ")
etiqueta_tamanoGB.place(x=10, y=130)
etiqueta_tamanoTB = ttk.Label(text="El tamaño en TB es: ")
etiqueta_tamanoTB.place(x=10, y=150)
etiqueta_dispositivosAlmacenamiento = ttk.Label(text="Memorias USB de 4 GB necesarias: ")
etiqueta_dispositivosAlmacenamiento.place(x=10, y=170)

ventana.mainloop()