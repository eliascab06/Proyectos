def main():
    frutas = []
    frutas.append("Mango")
    frutas.append("Manzana")
    frutas.append("Banana")
    frutas.append("Uva")
    print(frutas)

    frutas.pop(0)   # elimina "Mango"
    frutas.pop(1)   # ahora el índice 1 corresponde a "Banana"
    frutas.append("Sandia")
    print(frutas)

if __name__ == "__main__":
    main()
