from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    # check if the char already exists in the dic 
    # if new add char to dic and add count + 1 to value
    # if not new look up in dict and change value += 1
    counts = {}
    for char in word:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
