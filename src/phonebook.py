
class Phonebook:
    """
    Classe Phonebook
    """
    def __init__(self):
        #Inicializa a agenda telefônica com uma entrada predefinida
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """
        Adiciona um nome e número à agenda telefônica.

        :param name: Nome da pessoa em formato de string
        :param number: Número de telefone da pessoa em formato de string
        :return: 'Nome inválido', 'Número inválido', 'Número adicionado' ou 'Nome duplicado'

        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nme invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalio'
        if '%' in name:
            return 'Nome invalido'

        if len(number) < 0:
            return 'Numero invalid'

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'
        """

        invalid_chars = ['#', '@', '!', '$', '%']
        for char in invalid_chars:
            if char in name:
                return 'Nome inválido'

        if len(number) == 0:
            return 'Número inválido'

        if name not in self.entries:
        #Adiciona o nome e número fornecidos à agenda telefônica
            self.entries[name] = number
            return 'Número adicionado'
        else:
            return 'Nome duplicado'

    def lookup(self, name):
        """
         Busca o número de telefone de uma pessoa pelo nome.
        :param name: Nome da pessoa em formato de string
        :return: Número de telefone da pessoa ou 'Nome não encontrado'

         if '#' in name:
            return 'Nome invaldo'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nme invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome nvalido'

        return self.entries[name]
        """

        if name in self.entries:
        #Retorna o número de telefone correspondente ao nome fornecido
            return self.entries[name]
        else:
            return 'Nome não encontrado'

    def get_names(self):
        """
        Retorna uma lista com todos os nomes presentes na agenda telefônica.
        :return: Lista de nomes
        """
        return list(self.entries.keys())

    def get_numbers(self):
        """
        Retorna uma lista com todos os números presentes na agenda telefônica.
        :return: Lista de números
        """
        return list(self.entries.values())

    def clear(self):
        """
        Remove todas as entradas da agenda telefônica.
       :return: Mensagem de confirmação 'Phonebook limpado'
        """
        self.entries = {}
        return 'Phonebook limpado'

    def search(self, search_name):
        """
        Busca todas as entradas da agenda telefônica que contenham uma substring fornecida.
        :param search_name: Substring a ser pesquisada
        :return: Lista de resultados da pesquisa (dicionários contendo nome e número)
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name: number})
        return result

    def get_phonebook_sorted(self):
        """
        Retorna a agenda telefônica em ordem alfabética.
        :return: Agenda telefônica ordenada
        """
        return dict(sorted(self.entries.items()))

    def get_phonebook_reverse(self):
        """
        Retorna a agenda telefônica em ordem alfabética inversa.
        :return: Agenda telefônica em ordem reversa
        """
        return dict(sorted(self.entries.items(), reverse=True))

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'
