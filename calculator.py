class Calculator:
    """
    Clase que simula la lógica interna de una calculadora,
    manejando el estado de los operandos y las operaciones.
    """
    def __init__(self):
        # Inicializa el estado de la calculadora
        self.current_operand = '0'
        self.previous_operand = ''
        self.operation = None
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
        
        # Simula slice(0, -1) de JavaScript para eliminar el último carácter
        self.current_operand = self.current_operand[:-1]
        
        if self.current_operand == '':
            self.current_operand = '0'

    def append_number(self, number):
        """Agrega un dígito o el punto decimal al operando actual."""
        # Se asegura que la entrada sea string para manipulación
        number = str(number)
        
        if self.current_operand == 'Error':
            self.current_operand = '' 
            
        # Evita múltiples puntos decimales
        if number == '.' and '.' in self.current_operand:
            return
            
        # Maneja la sustitución del '0' inicial, similar al JS original
        if self.current_operand == '0' and number != '.':
            self.current_operand = number
        else:
            self.current_operand += number

    def choose_operation(self, operation):
        """
        Establece la operación. Si ya hay un operando previo,
        ejecuta el cálculo antes de establecer la nueva operación.
        """
        if self.current_operand == '0' and self.previous_operand == '':
            return
            
        # Si ya hay un cálculo pendiente, lo ejecuta
        if self.previous_operand != '':
            self.compute()
            
        self.operation = operation
        self.previous_operand = self.current_operand
        self.current_operand = '0' # Limpia para la nueva entrada

    @staticmethod
    def add(a, b):
        """Método estático para la suma (Unit Test Target)."""
        return a + b

    def compute(self):
        """Ejecuta el cálculo basado en la operación actual."""
        try:
            prev = float(self.previous_operand)
            current = float(self.current_operand)
        except ValueError:
            # Retorna si alguno de los operandos no es un número válido
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
                computation = 'Error' # Manejo de división por cero
            else:
                computation = prev / current
        else:
            return

        if computation == 'Error':
            self.current_operand = 'Error'
        else:
            # Convierte el resultado a string para mantener el flujo de entrada/salida
            self.current_operand = str(computation)
        
        self.operation = None
        self.previous_operand = ''

# Nota: En una aplicación de consola, se necesitaría una lógica de bucle
# de entrada y salida para simular la interfaz del usuario.