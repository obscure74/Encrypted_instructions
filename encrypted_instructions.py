# ID посылки: 146611402
def decode_instructions(compressed: str) -> str:
    """
    Раскодирует сжатую строку инструкций с повторениями в формате k[строка].
    
    Алгоритм использует рекурсивный подход для обработки вложенных структур.
    Примеры:
        "3[a]2[bc]" → "aaabcbc"
        "3[a2[c]]" → "accaccacc"
        "2[abc]3[cd]ef" → "abcabccdcdcdef"
    
    Args:
        compressed: сжатая строка в формате с повторениями
        
    Returns:
        Раскодированная строка
    """
    def decode_from_index(start_idx: int) -> tuple[str, int]:
        """
        Рекурсивно раскодирует подстроку начиная с заданной позиции.
        
        Args:
            start_idx: индекс начала раскодируемой подстроки
            
        Returns:
            Кортеж (раскодированная_подстрока, следующий_индекс)
        """
        decoded_parts: list[str] = []
        repeat_count: int = 0
        current_idx: int = start_idx
        
        while current_idx < len(compressed):
            current_char: str = compressed[current_idx]
            
            if current_char.isdigit():
                repeat_count = repeat_count * 10 + int(current_char)
                current_idx += 1
            elif current_char == '[':
                inner_decoded: str
                next_idx: int
                inner_decoded, next_idx = decode_from_index(current_idx + 1)
                decoded_part: str = (
                    inner_decoded * repeat_count 
                    if repeat_count > 0 
                    else inner_decoded
                )
                decoded_parts.append(decoded_part)
                repeat_count = 0
                current_idx = next_idx
            elif current_char == ']':
                return ''.join(decoded_parts), current_idx + 1
            else:
                decoded_parts.append(current_char)
                current_idx += 1
                repeat_count = 0
        
        return ''.join(decoded_parts), current_idx
    
    result: str
    result, _ = decode_from_index(0)
    return result


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
