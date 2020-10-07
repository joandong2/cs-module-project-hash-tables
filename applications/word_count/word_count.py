import re


def word_count(s):
    # # Your code here

    chars = r' " : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()
    filtered = ''.join([word.lower() for word in s if not word in chars])
    dict = {}
    for word in filtered.split():
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict


if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.cat'))
    # print(word_count(
    #     'This is a test of the emergency broadcast network. This is only a test.'))

    print(word_count('Hello, my cat.  And my cat doesn\'t say "hello" back.'))
    # print(word_count('":;,.-+=/\\|[]{}()*^&'))
