import tkinter as tk
from tkinter import messagebox
import time

class Calculator:
    """
    Clase que simula la lógica interna de la calculadora.
    Adaptada del código JavaScript original.
    """
    def __init__(self):
        self.clear()

    def clear(self):
        """Reinicia el estado de la calculadora (AC)."""
        self.current_operand = '0'
        self.previous_operand = ''
        self.operation = None

    def delete(self):
        """Elimina el último dígito del operando actual (DEL)."""
        if self.current_operand == 'Error' or self.current_operand == '0':
            return
        
        # Elimina el último carácter
        self.current_operand = self.current_operand[:-1]
        
        if self.current_operand == '':
            self.current_operand = '0'

    def append_number(self, number):
        """Agrega un dígito o el punto decimal al operando actual."""
        number = str(number)
        
        if self.current_operand == 'Error':
            self.current_operand = ''
            
        if number == '.' and '.' in self.current_operand:
            return
            
        if self.current_operand == '0' and number != '.':
            self.current_operand = number
        else:
            self.current_operand += number

    def choose_operation(self, operation):
        """
        Establece la operación. Ejecuta el cálculo si hay una operación pendiente.
        """
        if self.current_operand == '0' and self.previous_operand == '':
            return
            
        if self.previous_operand != '':
            self.compute()
            
        self.operation = operation
        self.previous_operand = self.current_operand
        self.current_operand = '0'

    @staticmethod
    def add(a, b):
        """Método estático para la suma."""
        return a + b

    def compute(self):
        """Ejecuta el cálculo basado en la operación actual."""
        try:
            prev = float(self.previous_operand)
            current = float(self.current_operand)
        except ValueError:
            return

        computation = None

        if self.operation == '+':
            computation = Calculator.add(prev, current)
        elif self.operation == '-':
            computation = prev - current
        elif self.operation == '*':
            computation = prev * current
        elif self.operation == '/':
            if current == 0:
                computation = 'Error'
            else:
                computation = prev / current
        else:
            return

        if computation == 'Error':
            self.current_operand = 'Error'
        else:
            # Elimina '.0' si el resultado es un entero
            if computation == int(computation):
                computation = int(computation)
            self.current_operand = str(computation)
        
        self.operation = None
        self.previous_operand = ''


class CalculatorGUI:
    """
    Interfaz gráfica de la calculadora usando Tkinter.
    """
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Minimalista (Python)")
        master.config(bg="#1e1e2e")  # Fondo oscuro del cuerpo (simulando style.css)
        
        # Centrar la ventana
        master.geometry("320x500")
        
        self.calculator = Calculator()
        
        # Marco principal para contener la calculadora
        self.calc_frame = tk.Frame(master, bg="#1e1e2e")
        self.calc_frame.pack(padx=20, pady=20)
        
        # --- Pantalla (Output) ---
        self.display_frame = tk.Frame(self.calc_frame, bg="#1e1e2e", height=120)
        self.display_frame.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(0, 20))
        self.display_frame.grid_propagate(False) # Evita que el frame se achique

        # Display anterior (operación pendiente)
        self.previous_label = tk.Label(self.display_frame, text="", anchor="se", justify="right",
                                       bg="#1e1e2e", fg="#C0C0C0", 
                                       font=("Poppins", 10), wraplength=280)
        self.previous_label.pack(fill="x", side="top", padx=10, pady=(10, 0))

        # Display actual (resultado o entrada)
        self.current_label = tk.Label(self.display_frame, text="0", anchor="se", justify="right",
                                      bg="#1e1e2e", fg="#fff", 
                                      font=("Poppins", 24, "bold"), wraplength=280)
        self.current_label.pack(fill="x", side="bottom", padx=10, pady=(0, 10))

        # --- Botones ---
        self.buttons_frame = tk.Frame(self.calc_frame, bg="#1e1e2e")
        self.buttons_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")

        # Configuración de estilo de botones (simulando style.css)
        self.default_btn_style = {'bg': '#2e2e3e', 'fg': '#fff', 'font': ('Poppins', 13), 'width': 5, 'height': 2, 'bd': 0, 'activebackground': '#3d3d52'}
        self.utility_btn_style = {'bg': '#ff6363', 'fg': '#fff', 'activebackground': '#ff4a4a'}
        self.operation_btn_style = {'bg': '#5563DE', 'fg': '#fff', 'activebackground': '#6b79f7'}
        self.equals_btn_style = {'bg': '#27ae60', 'fg': '#fff', 'activebackground': '#2ecc71'}

        # Definición y mapeo de botones (Grid de 4x5)
        # NOTA: Todos los elementos deben tener 6 valores (text, row, col, span, command, style_override)
        buttons = [
            # Fila 1
            ('AC', 0, 0, 2, self.clear_all, self.utility_btn_style),
            ('DEL', 0, 2, 1, self.delete_char, self.utility_btn_style),
            ('/', 0, 3, 1, lambda o='/': self.choose_op(o), self.operation_btn_style),
            
            # Fila 2
            ('7', 1, 0, 1, lambda n='7': self.append_num(n), None), # <--- CORREGIDO: Añadido None
            ('8', 1, 1, 1, lambda n='8': self.append_num(n), None), # <--- CORREGIDO: Añadido None
            ('9', 1, 2, 1, lambda n='9': self.append_num(n), None), # <--- CORREGIDO: Añadido None
            ('*', 1, 3, 1, lambda o='*': self.choose_op(o), self.operation_btn_style),
            
            # Fila 3
            ('4', 2, 0, 1, lambda n='4': self.append_num(n), None), # <--- CORREGIDO: Añadido None
            ('5', 2, 1, 1, lambda n='5': self.append_num(n), None), # <--- CORREGIDO: Añadido None
            ('6', 2, 2, 1, lambda n='6': self.append_num(n), None), # <--- CORREGIDO: Añadido None
            ('+', 2, 3, 1, lambda o='+': self.choose_op(o), self.operation_btn_style),
            
            # Fila 4
            ('1', 3, 0, 1, lambda n='1': self.append_num(n), None), # <--- CORREGIDO: Añadido None
            ('2', 3, 1, 1, lambda n='2': self.append_num(n), None), # <--- CORREGIDO: Añadido None
            ('3', 3, 2, 1, lambda n='3': self.append_num(n), None), # <--- CORREGIDO: Añadido None
            ('-', 3, 3, 1, lambda o='-': self.choose_op(o), self.operation_btn_style),
            
            # Fila 5
            ('.', 4, 0, 1, lambda n='.': self.append_num(n), None), # <--- CORREGIDO: Añadido None
            ('0', 4, 1, 1, lambda n='0': self.append_num(n), None), # <--- CORREGIDO: Añadido None
            ('=', 4, 2, 2, self.compute_result, self.equals_btn_style)
        ]

        # Creación de los botones en la cuadrícula
        for text, row, col, span, command, style_override in buttons:
            style = self.default_btn_style.copy()
            
            # Si hay un override de estilo (no es None), se actualiza
            if style_override: 
                style.update(style_override)
            
            button = tk.Button(self.buttons_frame, text=text, command=command, **style)
            button.grid(row=row, column=col, columnspan=span, sticky="nsew", padx=6, pady=6)
            
            # Asegura que las columnas se expandan por igual
            self.buttons_frame.grid_columnconfigure(col, weight=1)

        self.update_display()

    # --- Métodos de Conexión ---

    def update_display(self):
        """Actualiza las etiquetas de la GUI con el estado actual de la calculadora."""
        # Operando actual
        self.current_label.config(text=self.calculator.current_operand)
        
        # Operando anterior + Operación
        op_symbol = self.calculator.operation if self.calculator.operation else ""
        self.previous_label.config(text=self.calculator.previous_operand + op_symbol)

    def append_num(self, number):
        self.calculator.append_number(number)
        self.update_display()

    def choose_op(self, operation):
        self.calculator.choose_operation(operation)
        self.update_display()

    def compute_result(self):
        self.calculator.compute()
        self.update_display()

    def clear_all(self):
        self.calculator.clear()
        self.update_display()

    def delete_char(self):
        self.calculator.delete()
        self.update_display()


# --- Ejecución del Programa ---
if __name__ == "__main__":
    root = tk.Tk()
    # Deshabilita el redimensionamiento, simulando una interfaz fija
    root.resizable(False, False) 
    app = CalculatorGUI(root)
    root.mainloop()