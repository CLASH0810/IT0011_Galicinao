# Define sets based on the diagram
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# (a) Elements in A ∪ B (Union)
elements_A_union_B = A | B  # A ∪ B
print("Elements in A ∪ B:", elements_A_union_B, "Count:", len(elements_A_union_B))

# (b) Elements in B that are not in A or C (B - (A ∪ C))
elements_B_not_in_A_C = B - (A | C)
print("Elements in B - (A ∪ C):", elements_B_not_in_A_C, "Count:", len(elements_B_not_in_A_C))

# (c) Showing specific sets using set operations

# (i) {h, i, j, k} → Elements only in C but not in A or B
set_1 = C - (A | B)
print("Set {h, i, j, k}:", set_1)

# (ii) {c, d, f} → Elements in A ∩ C (intersection of A and C)
set_2 = A & C
print("Set {c, d, f}:", set_2)

# (iii) {b, c, h} → Elements in B ∩ (A ∪ C)
set_3 = B & (A | C)
print("Set {b, c, h}:", set_3)

# (iv) {d, f} → Elements in A ∩ C but not in B
set_4 = (A & C) - B
print("Set {d, f}:", set_4)

# (v) {c} → Elements in A ∩ B ∩ C (common in all three sets)
set_5 = A & B & C
print("Set {c}:", set_5)

# (vi) {l, m, o} → Elements only in B
set_6 = B - (A | C)
print("Set {l, m, o}:", set_6)
