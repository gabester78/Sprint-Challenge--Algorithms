'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    characters = "th"

    # Base case
    if len(word) <= 1:
        return 0

    # Use recursive to check if characters match
    if word[0:len(characters)] == characters:
        return count_th(word[1:])+1

    # Resume counting from remaining index
    return count_th(word[1:])


print(count_th('thsuperTHandTHth'))
