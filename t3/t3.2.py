def find_pair_sum_indices(numbers, target_sum):
    indices = {}
    pairs = {}

    for i, num in enumerate(numbers):
        complement = target_sum - num
        if complement in indices and complement != num:
            pair_sum = indices[complement] + i
            pairs[(complement, num)] = pair_sum

        indices[num] = i

    return pairs

def main():
    a = input()
    b = int(input())
    x = list(map(int, a.split()))

    pairs_dict = find_pair_sum_indices(x, b)

    if not pairs_dict:
        print("Not Found!")
    else:
        for pair_sum in sorted(pairs_dict.values()):
            print(pair_sum)

if __name__ == "__main__":
    main()


