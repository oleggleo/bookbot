count_words = lambda text: f'Found {len(text.split())} total words'

def count_chars(text):
    chars = {}

    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    return chars

def rearrange_dict(chars_dict):
    list_dict = []

    for key, value in chars_dict.items():
        list_dict.append({"char": key, "num": value})

    def sort_on(items):
        return items["num"]
    
    list_dict.sort(reverse=True, key=sort_on)

    return list_dict

    