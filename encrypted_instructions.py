# ID посылки: 146611402
def decode_instructions(compressed: str) -> str:
    """
    Раскодирует сжатую строку инструкций с повторениями в формате k[строка].
    
    Алгоритм использует стековый подход для обработки вложенных структур.
    Примеры:
        "3[a]2[bc]" → "aaabcbc"
        "3[a2[c]]" → "accaccacc"
        "2[abc]3[cd]ef" → "abcabccdcdcdef"
    
    Args:
        compressed: сжатая строка в формате с повторениями
        
    Returns:
        Раскодированная строка
    """
    stack: list[tuple[str, str]] = []  # (current_result, repeat_count)
    current_result: str = ""
    repeat_count_str: str = ""
        
    for char in compressed:
        if '0' <= char <= '9':
            # Собираем цифры в строку
            repeat_count_str += char
        elif char == '[':
            # Сохраняем текущее состояние в стек
            stack.append((current_result, repeat_count_str))
            current_result = ""
            repeat_count_str = ""
        elif char == ']':
            # Извлекаем предыдущее состояние из стека
            prev_result, prev_repeat_str = stack.pop()
            repeat_count = int(prev_repeat_str)
            current_result = prev_result + current_result * repeat_count
        else:
            # Обычный символ - добавляем к текущему результату
            current_result += char
        
        return current_result 


def main() -> None:
    """
    Основная функция программы.
    
    Читает сжатую строку из входных данных 
    и выводит раскодированную версию.
    """
    compressed_input: str = input().strip()
    print(decode_instructions(compressed_input))


if __name__ == "__main__":
    main()
