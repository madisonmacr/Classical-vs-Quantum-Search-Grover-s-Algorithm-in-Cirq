def classical_search(target, data):
    steps = 0
    for item in data:
        steps += 1
        if item == target:
            return steps

if __name__ == "__main__":
    data = [0, 1, 2, 3]
    target = 2

    steps = classical_search(target, data)
    print(f"Found target {target} in {steps} steps (classical search)")
