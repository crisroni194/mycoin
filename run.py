from blockchain import Blockchain, Transaction
from wallet import Wallet

def get_transaction_data():
    sender = input("Ingresa la dirección del remitente: ")
    recipient = input("Ingresa la dirección del destinatario: ")
    amount = float(input("Ingresa la cantidad de criptomoneda: "))
    return sender, recipient, amount

def main():
    blockchain = Blockchain()
    print("Bienvenido a la cadena de bloques de criptomoneda")
    print("Selecciona una opción:")
    print("1: Agregar transacción")
    print("2: Minar bloque")
    print("3: Mostrar cadena de bloques")
    print("4: Salir")
    print("5: Generar nueva dirección")
    while True:
        choice = input("Ingresa tu selección: ")
        if choice == "1":
            sender, recipient, amount = get_transaction_data()
            transaction = Transaction(sender, recipient, amount)
            if blockchain.add_transaction(transaction):
                print("Transacción agregada")
            else:
                print("Transacción fallida")
        elif choice == "2":
            if blockchain.mine_pending_transactions('miners-address'):
                print("Bloque minado exitosamente")
            else:
                print("Error al minar el bloque")
        elif choice == "3":
            blockchain.print_blocks()
        elif choice == "4":
            break
        elif choice == "5":
            address = Wallet.generate_new_address()
            print(f"Nueva dirección de billetera generada: {address}")
        else:
            print("Selección inválida")

if __name__ == '__main__':
    main()
    
    blockchain = Blockchain()
    blockchain.add_block("Block 1 data")
    blockchain.add_block("Block 2 data")
    blockchain.add_block("Block 3 data")
    blockchain.print_blocks()
