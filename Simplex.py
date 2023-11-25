class Simplex:
    def __init__(self):
        self.table = []

    def set_funcao_objetiva(self, fo: list ):
        self.table.append(fo)

    def add_restricoes(self, sa: list):
        self.table.append(sa)

    def get_entra_colunas(self) -> int:
        coluna_pivot = min(self.table[0])
        index = self.table[0].index(coluna_pivot)

        return index
    
    def get_sai_linha(self, entra_coluna: int) -> int:
        resultados = {}
        for line in range(len(self.table)):
            if line > 0:
                if self.table[line][entra_coluna] > 0:
                    divisao = self.table[line][-1] / self.table[line][entra_coluna]
                    resultados[line] = divisao
        index = min(resultados, key=resultados.get)

        return index
    
    def calcula_nova_linha_pivot(self, coluna_entrada: int, linha_saiu: int) -> list:
        linha =  self.table[linha_saiu]
        pivot = linha[coluna_entrada]
        nova_linha_pivot = [value / pivot for value in linha]

        return nova_linha_pivot

    def calcula_nova_linha(self, linha: list, coluna_entrada: int, linha_pivot: list) -> list:
        pivot = linha[coluna_entrada] * -1

        linha_resultado = [value * pivot for value in linha_pivot]

        nova_linha = []

        for i in range(len(linha_resultado)):
            soma_valor = linha_resultado[i] + linha[i]
            nova_linha.append(soma_valor)

        return nova_linha
    
    def is_negative(self) -> bool:
        negativo = list(filter(lambda x:x < 0, self.table[0]))

        return True if len(negativo) > 0 else False
    
    def get_variables(self):
        basic_variables = []
        non_basic_variables = []

        for i in range(1, len(self.table[0])-1):
            column = [row[i] for row in self.table[1:]]
            if column.count(0) == len(column) - 1 and column.count(1) == 1:
                basic_variables.append(f"x{i}")
            else:
                non_basic_variables.append(f"x{i}")

        return basic_variables, non_basic_variables

    def print_variables(self):
        basic_variables, non_basic_variables = self.get_variables()
        print(f"Variáveis básicas: {', '.join(basic_variables)}")
        print(f"Variáveis não básicas: {', '.join(non_basic_variables)}")
    
    
    def print_table(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                if j == len(self.table[0]) - 1:
                    print(f"{self.table[i][j]}\t", end="")
                else:
                    print(f"{self.table[i][j]}\t", end="")
            print()
        self.print_variables()
    
    def recalcula(self):
        coluna_entrada = self.get_entra_colunas()
        primeira_linha_saida = self.get_sai_linha(coluna_entrada)
        linha_pivot = self.calcula_nova_linha_pivot(coluna_entrada, primeira_linha_saida)
        self.table[primeira_linha_saida] = linha_pivot
        table_copy = self.table.copy()
        index = 0
        saida = []
        for i in range(len(self.table)):
            saida.append(self.table[i][-1])

        print("Variáveis básicas:", end=" ")
        for i in range(len(saida)):
            if saida[i] != 0:
                print(f"x{i+1}", end=" ")
        print()

        print("Variáveis não básicas:", end=" ")
        for i in range(len(saida)):
            if saida[i] == 0:
                print(f"x{i+1}", end=" ")
        print()

        print("Z:", saida[-1])
        
        while index < len(self.table):
            if index != primeira_linha_saida:
                line = table_copy[index]
                nova_linha = self.calcula_nova_linha(line, coluna_entrada, linha_pivot)
                self.table[index] = nova_linha
            index += 1
                
        


    def resolve(self):
        self.recalcula()

        while self.is_negative():
            self.recalcula()
        
        self.print_table()