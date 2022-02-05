import re


def textFix(text):
    result = re.sub('\.(?!\s)', '. ', text)
    if (result[len(result) - 1]) == ' ':
        return result[:-1]
    return result

def main():
    text = """Dog is eating rice.Cat is drinking milk.Bird is flying. """
    cleaned_text = textFix(text)
    print(cleaned_text)


if __name__ == '__main__':
    main()

