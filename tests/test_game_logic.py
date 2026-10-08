import pytest

from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# FIX: Asked Claude Code (agent mode) to write tests for the bugs we found.
# It also ran them against the old buggy code to make sure they actually fail.

# --- Regression tests for the reversed-hint bug ---

def test_too_high_guess_tells_player_to_go_lower():
    # Bug: a guess above the secret used to say "Go HIGHER!"
    _, message = check_guess(80, 40)
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_guess_tells_player_to_go_higher():
    # Bug: a guess below the secret used to say "Go LOWER!"
    _, message = check_guess(10, 40)
    assert "HIGHER" in message
    assert "LOWER" not in message


# --- Regression tests for the int-vs-string comparison bug ---

@pytest.mark.parametrize("guess, secret, expected", [
    (10, 40, "Too Low"),   # "10" < "40" as strings, and 10 < 40 as ints
    (9, 40, "Too Low"),    # "9" > "40" as strings, so string comparison says "Too High"
    (100, 20, "Too High"), # "100" < "20" as strings, so string comparison says "Too Low"
    (5, 50, "Too Low"),
    (50, 5, "Too High"),
])
def test_numeric_not_lexicographic_comparison(guess, secret, expected):
    # Bug: on even attempts the secret was converted to str, so guesses
    # were compared lexicographically instead of numerically.
    outcome, _ = check_guess(guess, secret)
    assert outcome == expected


def test_check_guess_does_not_rely_on_string_fallback():
    # The app now always passes an int secret; a str secret must not
    # silently produce a hint via string comparison.
    with pytest.raises(TypeError):
        check_guess(10, "40")
