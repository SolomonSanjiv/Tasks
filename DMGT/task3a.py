def union(set1, set2):
    return set1.union(set2)
def intersection(set1, set2):
    return set1.intersection(set2)
def difference(set1, set2):
    return set1.difference(set2)
def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)
def subset(set1, set2):
    return set1.issubset(set2)
def superset(set1, set2):
    return set1.issuperset(set2)
def main():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("\nUnion:", union(set1, set2))
    print("Intersection:", intersection(set1, set2))
    print("Difference (Set1 - Set2):", difference(set1, set2))
    print("Difference (Set2 - Set1):", difference(set2, set1))
    print("Symmetric Difference:", symmetric_difference(set1, set2))
    print("\nIs Set1 a subset of Set2?", subset(set1, set2))
    print("Is Set2 a subset of Set1?", subset(set2, set1))
    print("Is Set1 a superset of Set2?", superset(set1, set2))
    print("Is Set2 a superset of Set1?", superset(set2, set1))
if __name__ == "__main__":
    main()
