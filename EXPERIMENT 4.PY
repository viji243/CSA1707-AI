def cryptarithmetic(addends, result):
    # addends: list of strings, result: string
    letters = set(''.join(addends)+result)
    if len(letters) > 10: return None
    letters = list(letters)
    first_letters = {word[0] for word in addends + [result]}
    digits = '0123456789'
    def word_value(w, mapping):
        return int(''.join(mapping[c] for c in w))
    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))
        if any(mapping[c]=='0' for c in first_letters): continue
        try:
            s = sum(word_value(w, mapping) for w in addends)
            if s == word_value(result, mapping):
                return mapping
        except:
            pass
    return None
