class Adaline:
    # Inicializa o Adaline
    def __init__(self, num_inputs, learning_rate=0.1, num_epochs=100): 
        # Inicializa os pesos com 0
        self.weights = [0] * (num_inputs + 1) 
        self.learning_rate = learning_rate 
        self.num_epochs = num_epochs  

    def treino(self, X, y):
        for _ in range(self.num_epochs): # Para cada época
            for inputs, label in zip(X, y): # Para cada entrada e rótulo
                inputs = [1] + inputs  # Adiciona o viés (1) à entrada
                prediction = self.previsao(inputs) # Faz a previsão
                error = label - prediction # Calcula o erro
                self.weights = [w + self.learning_rate * error * x for w, x in zip(self.weights, inputs)] # Atualiza os pesos

    def previsao(self, inputs): # Faz a previsão
        summation = sum(w * x for w, x in zip(self.weights, inputs)) # Soma ponderada
        return 1 if summation >= 0 else 0 # Função de ativação

# Função OR
X_or = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_or = [0, 1, 1, 1]

Adaline_or = Adaline(2) #Cria um Adaline com 2 entradas
Adaline_or.treino(X_or, y_or) #Treina o Adaline

print("OR")
for inputs in X_or:
    inputs_with_bias = [1] + inputs #Adiciona o viés (1) à entrada
    prediction = Adaline_or.previsao(inputs_with_bias) #Faz a previsão
    print(f"Entrada: {inputs}, Saída: {prediction}") #Imprime o resultado

# Função AND
X_and = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_and = [0, 0, 0, 1]

Adaline_and = Adaline(2)
Adaline_and.treino(X_and, y_and)

print("\nAND")
for inputs in X_and:
    inputs_with_bias = [1] + inputs
    prediction = Adaline_and.previsao(inputs_with_bias)
    print(f"Entrada: {inputs}, Saída: {prediction}")

# Função NOT
X_not = [[0], [1]]
y_not = [1, 0]

Adaline_not = Adaline(1)
Adaline_not.treino(X_not, y_not)

print("\nNOT")
for inputs in X_not:
    inputs_with_bias = [1] + inputs
    prediction = Adaline_not.previsao(inputs_with_bias)
    print(f"Entrada: {inputs}, Saída: {prediction}")


# Função XOR
X_xor = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_xor = [0, 1, 1, 0]

Adaline_xor = Adaline(2) 
Adaline_xor.treino(X_xor, y_xor) 

print("XOR")
for inputs in X_xor:
    inputs_with_bias = [1] + inputs
    prediction = Adaline_xor.previsao(inputs_with_bias)
    print(f"Entrada: {inputs}, Saída: {prediction}")