import pytest

cnt = 0


@pytest.fixture(autouse=True)
def clean_text_file():
    global cnt
    with open('tests/testfile.txt', 'w'):
        pass
    print('\n' + str(cnt))
    cnt += 1
