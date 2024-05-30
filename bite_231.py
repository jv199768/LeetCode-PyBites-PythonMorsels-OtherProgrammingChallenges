import re
from typing import List

# https://stackoverflow.com/a/43147265
IS_EMOJI = re.compile(r'[^\w\s,]')


def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    emoji_list = re.findall(IS_EMOJI, text)
    indice = []

    for emoji in emoji_list:
        for char in re.finditer(emoji, text):
            position = char.start()
            if position not in indice:
                indice.append(position)
            else:
                pass
    

    return indice
