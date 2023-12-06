from abc import ABC, abstractmethod

class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano

    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return (
            self.__dia == outraData.__dia
            and self.__mes == outraData.__mes
            and self.__ano == outraData.__ano
        )

    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False

    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False


class AnaliseDados(ABC):
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados
        self.__lista = []

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass

    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass


class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []

    def entradaDeDados(self):
        n = int(input("Quantos nomes deseja inserir? "))
        for i in range(n):
            nome = input(f"Digite o nome {i+1}: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        sorted_list = sorted(self.__lista)
        length = len(sorted_list)
        median_index = length // 2
        print("Mediana:", sorted_list[median_index])

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))

    def listarEmOrdem(self):
        sorted_list = sorted(self.__lista)
        print("Lista em ordem:", sorted_list)


class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []

    def entradaDeDados(self):
        n = int(input("Quantas datas deseja inserir? "))
        for i in range(n):
            dia = int(input(f"Digite o dia {i+1}: "))
            mes = int(input(f"Digite o mês {i+1}: "))
            ano = int(input(f"Digite o ano {i+1}: "))
            data = Data(dia, mes, ano)
            self.__lista.append(data)

    def mostraMediana(self):
        sorted_list = sorted(self.__lista)
        length = len(sorted_list)
        median_index = length // 2
        print("Mediana:", sorted_list[median_index])

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))

    def listarEmOrdem(self):
        self.__lista.sort()
        print("Lista em ordem:")
        for data in self.__lista:
            print(data)


class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(type(float))
        self.__lista = []

    def entradaDeDados(self):
        n = int(input("Quantos salários deseja inserir? "))
        for i in range(n):
            salario = float(input(f"Digite o salário {i+1}: "))
            self.__lista.append(salario)

    def mostraMediana(self):
        sorted_list = sorted(self.__lista)
        length = len(sorted_list)
        median_index = length // 2
        median = sorted_list[median_index]
        if length % 2 == 0:  # Par
            median = (median + sorted_list[median_index - 1]) / 2
        print("Mediana:", median)

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))

    def listarEmOrdem(self):
        self.__lista.sort()
        print("Lista em ordem:", self.__lista)


class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []

    def entradaDeDados(self):
        n = int(input("Quantas idades deseja inserir? "))
        for i in range(n):
            idade = int(input(f"Digite a idade {i+1}: "))
            self.__lista.append(idade)

    def mostraMediana(self):
        sorted_list = sorted(self.__lista)
        length = len(sorted_list)
        median_index = length // 2
        median = sorted_list[median_index]
        if length % 2 == 0:  # Par
            median = (median + sorted_list[median_index - 1]) / 2
        print("Mediana:", median)

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))

    def listarEmOrdem(self):
        self.__lista.sort()
        print("Lista em ordem:", self.__lista)


def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    # Entrada de dados para as listas
    for lista in [nomes, datas, salarios, idades]:
        lista.entradaDeDados()

    listaListas = [nomes, datas, salarios, idades]

    # Exemplo de uso do iterador zip para percorrer listas de nomes e salários
    print("Iterador zip - Nome e Salário:")
    for nome, salario in zip(nomes._ListaNomes__lista, salarios._ListaSalarios__lista):
        print(f"Nome: {nome}, Salário: {salario}")
    print("___________________")

    # Exemplo de uso do iterador map para calcular reajuste de salários em 10%
    print("Iterador map - Reajuste de Salários:")
    salarios._ListaSalarios__lista = list(map(lambda x: x * 1.1, salarios._ListaSalarios__lista))
    print("Salários reajustados:", salarios._ListaSalarios__lista)
    print("___________________")

    # Exemplo de uso do iterador filter para modificar datas anteriores a 2019
    print("Iterador filter - Modificação de Datas:")
    datas._ListaDatas__lista = list(filter(lambda x: x.ano < 2019, datas._ListaDatas__lista))
    for data in datas._ListaDatas__lista:
        data.dia = 1
        print(data)
    print("___________________")

    # Executando as operações estatísticas nas listas
    for lista in listaListas:
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        lista.listarEmOrdem()
        print("___________________")

    print("Fim do teste!!!")


if __name__ == "__main__":
    main()

    #exercicio 2