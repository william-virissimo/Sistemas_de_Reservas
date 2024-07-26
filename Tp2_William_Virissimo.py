class node:
    def __init__(self,tipo_quarto,disponibilidade = True):
        self.tipo_quarto = tipo_quarto
        self.disponibilidade = disponibilidade
        self.direita = None
        self.esquerda = None 
class Sistema_reserva:
    def __init__(self):
        self.root = None
    def inserir_quarto(self,tipo_quarto):
        if not self.root:
            self.root = node(tipo_quarto)
        else:
            self.inserir_quarto_recursivo(tipo_quarto,self.root)
    def inserir_quarto_recursivo(self,tipo_quarto,current_node):
        if tipo_quarto < current_node.tipo_quarto:
            if current_node.esquerda:
                self.inserir_quarto_recursivo(tipo_quarto,current_node.esquerda)
            else:
                current_node.esquerda = node(tipo_quarto)
        elif tipo_quarto > current_node.tipo_quarto:
            if current_node.direita:
                self.inserir_quarto_recursivo(tipo_quarto,current_node.direita)
            else:
                current_node.direita = node(tipo_quarto)
    def disponibilidade_quarto(self,tipo_quarto):
        return self.disponibilidade_quarto_recursivo(tipo_quarto,self.root)
    def disponibilidade_quarto_recursivo(self,tipo_quarto,current_node):
        if current_node is None:
            return False
        if tipo_quarto == current_node.tipo_quarto:
            return current_node.disponibilidade
        elif tipo_quarto < current_node.tipo_quarto:
            return self.disponibilidade_quarto_recursivo(tipo_quarto,current_node.esquerda)
        else:
            return self.disponibilidade_quarto_recursivo(tipo_quarto,current_node.direita)
        
    def reserva_quarto(self,tipo_quarto):
        return self.reserva_quarto_recursivo(tipo_quarto,self.root)
    
    def reserva_quarto_recursivo(self,tipo_quarto,current_node):
        if current_node is None:
            return False
        if tipo_quarto == current_node.tipo_quarto:
            if current_node.disponibilidade:
                current_node.disponibilidade = False
                return True
            else:
                return False
        elif tipo_quarto < current_node.tipo_quarto:
            return self.reserva_quarto_recursivo(tipo_quarto,current_node.esquerda)
        else:
            return self.reserva_quarto_recursivo(tipo_quarto,current_node.direita)
def main():
    hotel_sistema = Sistema_reserva()

    hotel_sistema.inserir_quarto('Solteiro')
    hotel_sistema.inserir_quarto('Casal')
    hotel_sistema.inserir_quarto('Suite')


    while True:
        print("\n--- Sistema de Reserva de Quartos de Hotel ---")
        print("1. Verificar disponibilidade de um quarto")
        print("2. Reservar um quarto")
        print("3. Sair")

        choice = input('Escolha uma opção: ')

        if choice == '1':
            tipo_quarto = input('Digite o tipo de quarto (Solteiro/Casal/Suite): ')
            disponibilidade = hotel_sistema.disponibilidade_quarto(tipo_quarto)
            if disponibilidade:
                print('O quarto',tipo_quarto,'está disponivel.')
            else:
                print('O quarto',tipo_quarto,'não está disponivel.')
        elif choice == '2':
            tipo_quarto = input('Digite o quarto que deseja reservar (Solteiro/Casal/Suite): ')
            success = hotel_sistema.reserva_quarto(tipo_quarto)
            if success:
                print('Reserva do quarto ',tipo_quarto,'efetuada com sucesso.')
            else:
                print('O quarto',tipo_quarto,'não está disponível para reserva.')
        elif choice == '3':
            print("Obrigado por usar o sistema de reserva de quartos de hotel. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

            
if __name__ == "__main__":
    main()
