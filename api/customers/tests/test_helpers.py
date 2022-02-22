import pytest

from ...customers.helpers import phone_to_E164, is_in_rectangle, string_to_key

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("(61) 111122222", "+5561111122222"),
        ("(61) 111133333", "+5561111133333"),
        ("ABC(61)_111D1.4D4444", "+5561111144444")
    ]
)
def test_phone_to_E164(test_input, expected):
    assert phone_to_E164(test_input) == expected


@pytest.mark.parametrize(
    "test_bottom_left,test_top_right,test_point,expected",
    [
        ((-4,2), (-2,4), (-3,3), True),
        ((-4,2), (-2,4), (-4,4), True),
        ((-4,2), (-2,4), (-5,5), False)
    ]
)
def test_is_in_rectangle(
    test_bottom_left,
    test_top_right,
    test_point,
    expected
):
    result = is_in_rectangle(test_bottom_left,test_top_right,test_point)
    assert result == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("abc def", "abc_def"),
        ("ábç déf", "abc_def"),
        ("ãbcde f", "abcde_f")
    ]
)
def test_string_to_key(test_input, expected):
    result = string_to_key(test_input)
    assert result == expected
