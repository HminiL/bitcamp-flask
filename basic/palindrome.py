def str_to_list(payload: str) -> []:
    strs = [char for char in payload if char.isalnum()]
    '''
    strs = []
     for char in payload:
        if char.isalnum():
            strs.append(char.lower())
    return strs
    '''


def isPalindrome(ls: []) -> bool:
    while len(ls) > 1:
        if ls.pop(0) != ls.pop():
            return False


if __name__ == '__main__':
   str_to_list("race a car")


