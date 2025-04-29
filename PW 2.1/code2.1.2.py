def combination_sum2(candidates, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            backtrack(i + 1, path + [candidates[i]], target - candidates[i])

    candidates.sort()
    result = []
    backtrack(0, [], target)
    return result

candidates = [2, 5, 7]
target = 7
combinations = combination_sum2(candidates, target)

print(combinations)