from tkinter import *
from blockchain import Blockchain, Transaction

# Crear una instancia de la cadena de bloques
blockchain = Blockchain()

# Función para agregar una transacción a la cadena de bloques
def add_transaction():
    sender = sender_entry.get()
    recipient = recipient_entry.get()
    amount = amount_entry.get()
    transaction = Transaction(sender, recipient, amount)
    blockchain.add_transaction(transaction)
    transaction_label.config(text="Última transacción: {}".format(transaction.to_dict()))

# Función para minar un bloque en la cadena de bloques
def mine_block():
    miner_address = miner_address_entry.get()
    blockchain.mine_pending_transactions(miner_address)
    chain_label.config(text="{}".format(blockchain.to_dict()))

# Configurar la ventana principal de la GUI
root = Tk()
root.title("ChainCoin")

# Etiquetas y campos de entrada para agregar una transacción
sender_label = Label(root, text="Remitente:")
sender_label.grid(row=0, column=0, sticky=E)
sender_entry = Entry(root)
sender_entry.grid(row=0, column=1)

recipient_label = Label(root, text="Destinatario:")
recipient_label.grid(row=1, column=0, sticky=E)
recipient_entry = Entry(root)
recipient_entry.grid(row=1, column=1)

amount_label = Label(root, text="Cantidad:")
amount_label.grid(row=2, column=0, sticky=E)
amount_entry = Entry(root)
amount_entry.grid(row=2, column=1)

add_button = Button(root, text="Agregar transacción", command=add_transaction)
add_button.grid(row=3, column=1)

transaction_label = Label(root, text="Última transacción:")
transaction_label.grid(row=4, column=1)

# Etiquetas y campos de entrada para minar un bloque
miner_address_label = Label(root, text="Dirección del minero:")
miner_address_label.grid(row=5, column=0, sticky=E)
miner_address_entry = Entry(root)
miner_address_entry.grid(row=5, column=1)

mine_button = Button(root, text="Minar bloque", command=mine_block)
mine_button.grid(row=6, column=1)

chain_label = Label(root, text="{}".format(blockchain.to_dict()))
chain_label.grid(row=7, column=1)

root.mainloop()
