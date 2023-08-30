import csv

class AgendaHeroes:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return ord(key[0]) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index].append((key, value))

    def find(self, key):
        index = self._hash_function(key)
        for stored_key, value in self.table[index]:
            if stored_key == key:
                return value
        return None

    def search_by_letter(self, letter):
        index = self._hash_function(letter)
        items_with_letter = []
        for stored_key, value in self.table[index]:
            if stored_key[0] == letter:
                items_with_letter.append((stored_key, value))
        return items_with_letter
    
    def search_by_name(self, name):
        for index in range(self.size):
            for stored_key, value in self.table[index]:
                if stored_key.lower() == name.lower():
                    return (stored_key, value)
        return None
    
    def remove(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                return True
        return False

def import_csv_to_hash_table(file_path, hash_table):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Pule a linha de cabeçalho
        for row in csv_reader:
            key = row[0]
            value = row[1]
            hash_table.insert(key, value)

def main():
    hash_table_size = 100  # You can adjust this size as needed
    hash_table = AgendaHeroes(hash_table_size)

    csv_file_path = input("Diretorio do arquivo csv: ")
    #Downloads/agenda.csv
    import_csv_to_hash_table(csv_file_path, hash_table)
    print("Dados do CSV importados!")

    while True:
        print("\nMenu:")
        print("1. Adicionar contato")
        print("2. Busca por letra")
        print("3. Busca por nome")
        print("4. Todos os contatos")
        print("5. Remover Contato")
        print("6. Sair")

        option = input("Opção: ")

        if option == '1':
            key = input("Nome: ")
            value = input("Telefone: ")
            hash_table.insert(key, value)
            print("Ok!")

        elif option == '2':
            letter = input("Digite a Letra para buscar na agenda: ")
            results = hash_table.search_by_letter(letter)
            if results:
                for key, value in results:
                    print(f"Nome: {key}, Telefone: {value}")
            else:
                print("Não existem resultados.")

        elif option == '3':
            name = input("Digite o Nome para buscar na agenda: ")
            result = hash_table.search_by_name(name)
            if result:
                print(f"Nome: {result[0]}, Telefone: {result[1]}")
            else:
                print("Contato não encontrado.")

        elif option == '4':
            print(hash_table.table)
        
        elif option == '5':
            key = input("Nome da pessoa que deseja remover da agenda: ")
            if hash_table.remove(key):
                print("Pessoa Removida com sucesso!")
            else:
                print("Pessoa não encontrada.")

        elif option == '6':
            print("Até mais!")
            break

        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
