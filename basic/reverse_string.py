def str_to_list(payload: str) -> []:
    return [char for char in payload if char.isalnum()]


def reverse_list(ls: []) -> []:
    return ls[::-1]


def list_to_str(ls: []) -> str:
    return ''.join(ls)


def reverseString(strs: []) -> []:
    return strs[::-1]


if __name__ == '__main__':
    #print(reverseString("안녕하세요"))
    print(str_to_list("hello"))
    print(reverse_list(str_to_list('hello')))
    print(list_to_str(reverse_list(str_to_list('hello'))))
    print(reverse_list('hello'))

