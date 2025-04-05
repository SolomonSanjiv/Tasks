def is_reflexive(relation, set):
    for element in set:
        if (element, element) not in relation:
            return False
    return True
def is_symmetric(relation):
    for pair in relation:
        if (pair[1], pair[0]) not in relation:
            return False
    return True
def is_transitive(relation):
    for pair1 in relation:
        for pair2 in relation:
            if pair1[1] == pair2[0] and (pair1[0], pair2[1]) not in relation:
                return False
    return True
def main():
    set = {1, 2, 3}
    relation = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
    print("Set:", set)
    print("Relation:", relation)
    print("\nIs Reflexive?", is_reflexive(relation, set))
    print("Is Symmetric?", is_symmetric(relation))
    print("Is Transitive?", is_transitive(relation))
if __name__ == "__main__":
    main()
