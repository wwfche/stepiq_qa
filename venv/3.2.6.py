#assert использование + добавление сообщения с ошибкой
assert abs(-42) == 42 , "Should be absolute value of a number" #сделай -42

actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something wrong")

print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

actual_result = "abrakadabra"
f"Wrong text, got {actual_result}, something wrong"



s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

# assert "login" in browser.current_url,  # сообщение об ошибке  проверяет есть ли логин в урле


def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

    #проверяет фразу на вхождение в строку, выводит необходимую ошибку
def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"