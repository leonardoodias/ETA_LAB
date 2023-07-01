from src.phonebook import Phonebook

class TestPhonebook:

    def test_add_success(self):
        # Testa a adição de um número de telefone válido
        phone = Phonebook()
        result = phone.add('Joao', '123456789')
        expected = "Número adicionado"
        assert result == expected

    def test_add_invalid_name(self):
        # Testa a adição de um nome inválido
        phone = Phonebook()
        result = phone.add('Joao#', '123456789')
        expected = 'Nome inválido'
        assert result == expected

    def test_add_duplicate_name(self):
        # Testa a adição de um nome duplicado
        phone = Phonebook()
        phone.add('Joao', '123456789')
        expected = 'Nome duplicado'
        result = phone.add('Joao', '987654321')
        assert result == expected

    def test_add_invalid_number(self):
        # Testa a adição de um número de telefone inválido
        phone = Phonebook()
        result = phone.add('Joao', '')
        expected = 'Número inválido'
        assert result == expected

    def test_add_invalid_name_character(self):
        # Testa a adição de um nome inválido com caracteres especiais
        phone = Phonebook()
        expected = 'Nome inválido'
        characters = ['Joao!', 'Joa@', 'Joa$o', 'Joao%', 'J#oao']
        for name in characters:
            result = phone.add(name, '123456789')
            assert result == expected

    def test_get_names(self):
        # Testa a obtenção de nomes do telefone
        phone = Phonebook()
        expected = ['POLICIA']
        result = phone.get_names()
        assert result == expected

    def test_get_numbers(self):
        # Testa a obtenção de números do telefone
        phone = Phonebook()
        expected = ['190']
        result = phone.get_numbers()
        assert result == expected

    def test_clear(self):
        # Testa a limpeza do telefone
        phone = Phonebook()
        phone.add('Joao', '123456789')
        expected = 'Phonebook limpado'
        result = phone.clear()
        assert result == expected

    def test_search_success(self):
        # Testa a busca de um nome no telefone
        phone = Phonebook()
        phone.add('Maria', '123456789')
        expected = [{'Maria': '123456789'}]
        result = phone.search('Maria')
        assert result == expected

    def test_search_success2(self):
        # Testa a busca de um nome no telefone
        phone = Phonebook()
        expected = [{'Leonardo': '123456'}]
        entries = {'Leonardo': '123456', 'Filipe': '123456789', 'Rosa': '123456789'}
        for name, number in entries.items():
            phone.add(name, number)

        result = phone.search('Leonardo')
        assert result == expected

    def test_search_partial_name(self):
        # Testa a busca por um nome parcial
        phone = Phonebook()
        expected = [{'Joao': '123456789'}, {'Joana': '987654321'}]
        phone.add('Joao', '123456789')
        phone.add('Joana', '987654321')
        result = phone.search('Jo')
        assert result == expected

    def test_search_not_found(self):
        # Testa a busca de um nome que não existe no telefone
        phone = Phonebook()
        expected = []

        result = phone.search('Giovani')
        assert result == expected

    def test_search_not_found2(self):
        # Testa a busca de um nome que não existe no telefone
        phone = Phonebook()
        expected = []
        contact_list = {'Leonardo': '123456', 'Joao': '123456789', 'Maria': '123456789'}
        for name, number in contact_list.items():
            phone.add(name, number)
        result = phone.search('Goku')
        assert result == expected

    def test_get_phonebook_sorted(self):
        # Testa a ordenação do telefone
        phone = Phonebook()
        expected = {'POLICIA': '190'}
        result = phone.get_phonebook_sorted()
        assert result == expected

    def test_get_phonebook_sorted2(self):
        # Testa a ordenação do telefone
        phone = Phonebook()
        expected = {'POLICIA': '190', 'BOMBEIROS': '193'}
        phone.add('BOMBEIROS', '193')
        result = phone.get_phonebook_sorted()
        assert result == expected

    def test_get_phonebook_sorted3(self):
        # Testa a ordenação do telefone
        phone = Phonebook()
        expected = {'POLICIA': '190', 'BOMBEIROS': '193', 'SAMU': '192'}
        phone.add('BOMBEIROS', '193')
        phone.add('SAMU', '192')
        result = phone.get_phonebook_sorted()
        assert result == expected

    def test_get_phonebook_sorted4(self):
        # Testa a ordenação do telefone
        phone = Phonebook()
        expected = {'POLICIA': '190', 'BOMBEIROS': '193', 'SAMU': '192', 'JOAO': '123456789'}
        phone.add('BOMBEIROS', '193')
        phone.add('SAMU', '192')
        phone.add('JOAO', '123456789')
        result = phone.get_phonebook_sorted()
        assert result == expected

    def test_get_phonebook_reverse(self):
        # Testa a ordenação reversa do telefone
        phone = Phonebook()
        expected = {'POLICIA': '190'}
        result = phone.get_phonebook_reverse()
        assert result == expected

    def test_get_phonebook_reverse2(self):
        # Testa a ordenação reversa do telefone
        phone = Phonebook()
        expected = {'POLICIA': '190', 'BOMBEIROS': '193'}
        phone.add('BOMBEIROS', '193')
        result = phone.get_phonebook_reverse()
        assert result == expected

    def test_delete_success(self):
        # Testa a deleção de um contato
        phone = Phonebook()
        phone.add('Joao', '123456789')
        expected = 'Número deletado'
        result = phone.delete('Joao')
        assert result == expected

    def test_delete_contact_not_found(self):
        # Testa a deleção de um contato que não existe
        phone = Phonebook()
        expected = 'Nome não encontrado'
        result = phone.delete('Joao')
        assert result == expected

    def test_delete_contact_not_found2(self):
        # Testa a deleção de um contato que não existe
        phone = Phonebook()
        phone.add('Joao', '123456789')
        expected = 'Nome não encontrado'
        result = phone.delete('Maria')
        assert result == expected

    def test_change_number_sucess(self):
        # Testa a alteração de um número de telefone
        phone = Phonebook()
        phone.add('Joao', '123456789')
        expected = 'Número alterado'
        result = phone.change_number('Joao', '987654321')
        assert result == expected

    def test_change_number_contact_not_found(self):
        # Testa a alteração de um número de telefone de um contato que não existe
        phone = Phonebook()
        expected = 'Nome não encontrado'
        result = phone.change_number('Joao', '987654321')
        assert result == expected

    def test_get_name_by_number_success(self):
        # Testa a obtenção de um nome pelo número de telefone
        phone = Phonebook()
        phone.add('Joao', '123456789')
        expected = 'Joao'
        result = phone.get_name_by_number('123456789')
        assert result == expected

    def test_get_name_by_number_not_found(self):
        # Testa a obtenção de um nome pelo número de telefone
        phone = Phonebook()
        expected = 'Número não encontrado'
        result = phone.get_name_by_number('123456789')
        assert result == expected