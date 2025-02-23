

def displayGrowth(initialAmount, contribution, growth):
    results = [initialAmount]
    for i in range(1,31):
        value = results[i-1] * (1+growth) + contribution
        results.append(value)
        print(f"Value {i} years later: {round(results[i])}")



def main():
    displayGrowth(30000, 7000, 0.01)



if __name__ == "__main__":
    main()