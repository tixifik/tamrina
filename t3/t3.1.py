def format_text(text):
    result = []
    at_count = 0

    for char in text:
        if char == '@':
            result.append(char)
            at_count += 1
        elif char == '#' and at_count > 0:
            at_count -= 1
        else:
            result.append(char)

    return ''.join(result)

def main():
    input_text = input()
    formatted_text = format_text(input_text)
    cleaned_text = " ".join(formatted_text.split())
    result = cleaned_text.replace('\\n', '\n')

    print(f"Formatted Text: {result}")

if __name__ == "__main__":
    main()




