from io import StringIO
import unittest
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent))
from game import get_input

class TestGame(unittest.TestCase):

    def _get_input(self, choices, inputs):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = inputs
            captured_output = StringIO()
            sys.stdout = captured_output
            act_val = get_input(choices)
            sys.stdout = sys.__stdout__
            act_out = captured_output.getvalue().strip().splitlines()
            exp_out = ["INVALID CHOICE"] * (len(inputs) - 1)
            exp_val = inputs[-1].strip().lower()
            message = f"""
I called get_input('{choices}').
I typed in:
{'\n'.join(inputs)}
I expected to see:
{'\n'.join(exp_out)}
And to get back the value: {exp_val}
I saw:
{'\n'.join(act_out)}
and got back: {act_val}
"""
            self.assertEqual(exp_val, act_val, message)
            invalid_count = 0
            for line in act_out:
                if "invalid" in line.lower():
                    invalid_count += 1
            self.assertEqual(len(inputs)-1, invalid_count, message)

    def test_get_input_returns_input_first_option(self):
        self._get_input('xyz',['x'])

    def test_get_input_returns_input_last_option(self):
        self._get_input('xyz',['z'])

    def test_get_input_options_capitalized(self):
        self._get_input('ABC',['c'])

    def test_get_input_inputs_capitalized(self):
        self._get_input('ABC',['A'])

    def test_get_input_returns_one_blank(self):
        self._get_input('xyz',['','x'])

    def test_get_input_returns_one_wrong(self):
        self._get_input('xyz',['a','x'])

    def test_get_input_returns_one_wrong_one_blank(self):
        self._get_input('xyz',['a','','x'])

    def test_get_input_one_too_long(self):
        self._get_input('xyz',['long','x'])

    def test_get_input_one_too_long_but_in_choices(self):
        self._get_input('xyz',['xy','x'])

    def test_get_input_strips_input(self):
        self._get_input('xyz',[' x'])

    def test_get_input_choices_blank(self):
        with self.assertRaises(
            ValueError,
            msg="I expected to see a ValueError raised when I called get_input('') (an empty string)"
        ):
            self._get_input(
                '',
                ['x']
            )

    def test_get_input_choices_only_has_spaces(self):
        with self.assertRaises(
            ValueError,
            msg="I expected to see a ValueError raised when I called get_input('  ') (only spaces)"
        ):
            self._get_input(
                '  ',
                ['x']
            )

    def test_get_input_choices_number(self):
        with self.assertRaises(
            ValueError,
            msg="I expected to see a ValueError raised when I called get_input(5) (or any number)"
        ):
            self._get_input(
                5,
                ['x']
            )

    def test_get_input_choices_none(self):
        with self.assertRaises(
            ValueError,
            msg="I expected to see a ValueError raised when I called get_input(None)"
        ):
            self._get_input(
                5,
                ['x']
            )

if __name__ == '__main__':
    unittest.main()
