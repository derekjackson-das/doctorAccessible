"""Checks tools/readability.py against hand counts on three samples.

Run: python -m unittest tools/test_readability.py   (from the repo root)

Each sample was counted by hand, word by word, before the tool was run. The
counts and the grade they give (the formula in readability.py) are below.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import readability as rd  # noqa: E402

HERE = os.path.join(os.path.dirname(__file__), "samples")

# Hand counts. Syllables per word are listed so a reader can check them.
HAND = {
    # The(1) library(3) opens(2) at(1) nine(1).
    # You(1) can(1) borrow(2) ten(1) books(1) at(1) a(1) time(1).
    # Bring(1) your(1) card(1) to(1) the(1) desk(1).
    "a-plain.txt": {"words": 19, "sentences": 3, "syllables": 23, "grade": 1.2},
    # Navigation, the h1, and the code block are left out.
    # Applications(4) submitted(3) after(2) the(1) deadline(2) require(2) written(2)
    # approval(3) from(1) the(1) department(3) administrator(5).
    # Approval(3) decisions(3) are(1) communicated(5) by(1) email(2).
    "b-dense.html": {"words": 18, "sentences": 2, "syllables": 44, "grade": 16.8},
    # The h2 and the button are left out; each list item is one sentence.
    # Silent(2) study(2) rooms(1) / Late(1) opening(3) on(1) Fridays(2) /
    # Open(2) until(2) ten(1) at(1) night(1) on(1) weekdays(2).
    "c-list.html": {"words": 14, "sentences": 3, "syllables": 22, "grade": 4.8},
}


def run(name):
    path = os.path.join(HERE, name)
    src = open(path, encoding="utf-8").read()
    blocks = rd.extract_html(src)[0] if name.endswith(".html") else [" ".join(src.split())]
    return rd.measure(blocks)


class HandCounts(unittest.TestCase):
    def test_samples(self):
        for name, want in HAND.items():
            with self.subTest(sample=name):
                got = run(name)
                self.assertEqual(got["words"], want["words"])
                self.assertEqual(got["sentences"], want["sentences"])
                self.assertEqual(got["syllables"], want["syllables"])
                self.assertAlmostEqual(round(got["grade"], 1), want["grade"])

    def test_abbreviation_does_not_end_a_sentence(self):
        self.assertEqual(len(rd.split_sentences("Open until 9 p.m. on weekdays.")), 1)

    def test_silent_endings(self):
        for word, n in {"time": 1, "the": 1, "table": 2, "opened": 2, "wanted": 2,
                        "times": 1, "boxes": 2, "you": 1, "study": 2}.items():
            with self.subTest(word=word):
                self.assertEqual(rd.count_syllables(word), n)


if __name__ == "__main__":
    unittest.main()
