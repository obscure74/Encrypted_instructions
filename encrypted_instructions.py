# ID посылки: 146611402
from string import digits


def decode_instructions(compressed: str) -> str:
    """
    Раскодирует сжатую строку инструкций с повторениями в формате k[строка].
    
    Алгоритм использует стековый подход для обработки вложенных структур.
    Каждый элемент стека содержит кортеж из текущего результата и счетчика повторений.
    Примеры:
        "3[a]2[bc]" → "aaabcbc"
        "3[a2[c]]" → "accaccacc"
        "2[abc]3[cd]ef" → "abcabccdcdcdef"
    
    Args:
        compressed: сжатая строка в формате с повторениями
        
    Returns:
        Раскодированная строка
    """
    digit_characters = set(digits)
    stack = []
    result_builder = ""
    repeat_digits = ""
        
    for char in compressed:
        if char in digit_characters:
            repeat_digits += char
        elif char == '[':
            stack.append((result_builder, repeat_digits))
            result_builder = ""
            repeat_digits = ""
        elif char == ']':
            previous_result, previous_repeat = stack.pop()
            repeat_count = int(previous_repeat)
            result_builder = previous_result + result_builder * repeat_count
        else:
            result_builder += char
    
    return result_builder


def main() -> None:
    """
    Основная функция программы.
    
    Читает сжатую строку из входных данных 
    и выводит раскодированную версию.
    """
    compressed_input = input().strip()
    print(decode_instructions(compressed_input))


if __name__ == "__main__":
    main()
