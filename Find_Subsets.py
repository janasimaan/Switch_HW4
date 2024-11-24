def find_subsets(lst):
    if lst==[]:
        return [[]]
    subsets_without_firstElem = find_subsets(lst[1:])
    return subsets_without_firstElem + [[lst[0]] + subset for subset in subsets_without_firstElem]


print(find_subsets([1, 2, 3]))



