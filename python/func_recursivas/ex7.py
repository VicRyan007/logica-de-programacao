def soma_digitos(numero):
    if numero < 10:
        return numero
    else:
        ultimo_digito = numero % 10
        numero_sem_ultimo_digito = numero // 10
        return ultimo_digito + soma_digitos(numero_sem_ultimo_digito)



print(soma_digitos(123))