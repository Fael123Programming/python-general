if __name__ == "__main__":
    try:
        raise ValueError("Value error")
    except ValueError:
        print("Dentro do bloco except")
        raise  # Lanca a excecao novamente
