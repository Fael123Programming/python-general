from collections import Counter


if __name__ == "__main__":
    data = ["Camaro SS", "Lamborghini Aventador", "Bugatti Veyron", "Camaro SS", "Ford F-150 Raptor", "Camaro SS",
            "Lamborghini Aventador", 90, 90]
    counter = Counter(data)
    print(counter)
