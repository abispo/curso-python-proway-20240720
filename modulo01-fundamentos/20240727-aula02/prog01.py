# match case

if __name__ == "__main__":

    acesso = input("Informe o seu nivel de acesso: ")

    match acesso.upper():
        case "USUARIO":
            print("Você possui um nível de acesso básico.")

        case "GESTOR":
            print("Você possui um nível de acesso intermediário.")

        case "ADMIN":
            print("Você possui acesso total.")

        case _:
            print("Acesso não reconhecido.")
