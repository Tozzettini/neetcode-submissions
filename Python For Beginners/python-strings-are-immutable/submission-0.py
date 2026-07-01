def remove_fourth_character(word: str) -> str:
    result = ""            
    # loops through the char
    for i in range(len(word)):
        if (i + 1) == 4:
            continue
        result += word[i]              
    return result



# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
