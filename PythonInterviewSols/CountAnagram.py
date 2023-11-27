from collections import Counter

def count_anagram_substrings(A, B):
  result = []

  for pattern in B:
    pattern_length = len(pattern)
    pattern_counter = Counter(pattern)
    window_counter = Counter(A[:pattern_length])

    count = 0
    if window_counter == pattern_counter:
      count += 1

    for i in range(pattern_length, len(A)):
      left_char, right_char = A[i - pattern_length], A[i]
      window_counter[left_char] -= 1
      if window_counter[left_char] == 0:
        del window_counter[left_char]
      window_counter[right_char] += 1

      if window_counter == pattern_counter:
        count += 1

    result.append(count)

  return result

print(count_anagram_substrings('jdlidfa',[ "afd", "ifd", "dxzjbltsmufythgm"]))
print(count_anagram_substrings('abcabdfedxdeyx',["abc","def","xy"]))