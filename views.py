from django.shortcuts import render
from django.http import HttpResponse
from .models import Wallet, Transaction

def home(request):
    # Obtener la billetera del usuario actual (asumiendo que hay autenticación)
    wallet = Wallet.objects.get(owner=request.user)

    # Obtener el balance de la billetera
    balance = wallet.get_balance()

    # Renderizar la plantilla y pasarle el balance como contexto
    return render(request, 'home.html', {'balance': balance})

def new_transaction(request):
    if request.method == 'POST':
        # Obtener los datos del formulario de la transacción
        sender_address = request.POST['sender_address']
        recipient_address = request.POST['recipient_address']
        value = request.POST['value']

        # Crear una nueva transacción
        transaction = Transaction(sender_address=sender_address, recipient_address=recipient_address, value=value)

        # Firmar la transacción con la clave privada de la billetera del remitente
        wallet = Wallet.objects.get(address=sender_address)
        signature = wallet.sign_transaction(transaction)

        # Añadir la firma a la transacción y guardarla en la base de datos
        transaction.signature = signature
        transaction.save()

        # Redirigir al usuario a la página de inicio
        return redirect('home')
    
    # Si el método de solicitud es GET, simplemente renderizar la plantilla del formulario
    return render(request, 'new_transaction.html')
