def get_num_words(text):
    words = text.split()
    return f"Found {len(words)} total words"


def get_num_characters(text):
    count = {}
    for char in text:
        if char.lower() in count:
            count[char.lower()] += 1
        else:
            count[char.lower()] = 1
    return count


def sorted_char_count(char_count_dict):
    filtered_dict = {k: v for k, v in char_count_dict.items() if k.isalpha()}
    ordered = dict(
        sorted(filtered_dict.items(), key=lambda item: item[1], reverse=True)
    )
    return [{k: v} for k, v in ordered.items()]
