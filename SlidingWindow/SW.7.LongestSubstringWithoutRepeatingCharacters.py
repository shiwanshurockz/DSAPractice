def longestUniqueSubsttr(self, S):
    # code here
    mapping = dict()
    n = len(S)
    i = 0
    maxLength = -1
    for j in range(n):
        if S[j] not in mapping:
            mapping[S[j]] = 1
        else:
            mapping[S[j]] += 1
        if len(mapping) == j - i + 1:
            maxLength = max(maxLength, j - i + 1)
        if len(mapping) < j - i + 1:
            if S[i] in mapping:
                mapping[S[i]] -= 1
                if mapping[S[i]] == 0:
                    mapping.pop(S[i])
            i += 1
    return maxLength