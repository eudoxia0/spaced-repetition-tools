#!/usr/bin/env python
import csv
import sys
from dataclasses import dataclass

# Types.


@dataclass(frozen=True)
class Elem:
    """
    An element in the sequence.
    """

    # Indices are humanized: the first card has index 1.
    index: int
    text: str

    def __post_init__(self):
        assert self.index > 0


@dataclass(frozen=True)
class Card:
    """
    A flashcard.
    """

    text: str


# Main loop.


def main():
    # Read all lines from stdin.
    lines: list[str] = [line.strip() for line in sys.stdin.readlines()]
    # The first line is the title of the sequence.
    title: str = lines[0]
    # The remaining lines are the elements of the sequence.
    elems: list[Elem] = [
        Elem(index=index + 1, text=text) for index, text in enumerate(lines[1:])
    ]
    # Accumulator for generated cards.
    cards: list[Card] = []
    # Make the test card. This asks us to recall the entire sequence from
    # beginning to end.
    cards.append(make_test_card(elems))
    # Make the cloze card. This has the entire sequence, with each item having a
    # separate cloze deletion.
    cards.append(make_cloze_card(elems))
    # The forward cards ask you to recall the element for a given index.
    cards += make_forward(elems)
    # The backwarrd cards ask you to recall the index for a given position.
    cards += make_backward(elems)
    # The successor cards ask you to remember what element comes after each.
    cards += make_successor(elems)
    # The predecessor cards ask you to remember what element comes before each.
    cards += make_predecessor(elems)
    # Render cards.
    writer = csv.writer(
        sys.stdout,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator="\n",
    )
    for card in cards:
        writer.writerow([render_card(card, title)])


def make_test_card(elems: list[Elem]) -> Card:
    lst: str = "\n".join("1. " + elem.text for elem in elems)
    text: str = f"Recall all elements of the sequence.\n---\n{lst}"
    return Card(text=text)


def make_cloze_card(elems: list[Elem]) -> Card:
    lst: str = "\n".join(
        "1. {{" + str(idx + 1) + "::" + elem.text + "}}"
        for idx, elem in enumerate(elems)
    )
    text: str = f"Elements of the sequence.\n---\n{lst}"
    return Card(text=text)


def render_card(card: Card, title: str) -> str:
    return f"# {title}\n\n{card.text}"


def make_forward(elems: list[Elem]) -> list[Card]:
    cards: list[Card] = []
    for elem in elems:
        text: str = f"What element has position {elem.index}?\n---\n{elem.text}"
        cards.append(Card(text=text))
    return cards


def make_backward(elems: list[Elem]) -> list[Card]:
    cards: list[Card] = []
    for elem in elems:
        text: str = f"What is the position of: {elem.text}\n---\n{elem.index}"
        cards.append(Card(text=text))
    return cards


def make_successor(elems: list[Elem]) -> list[Card]:
    cards: list[Card] = []
    for pos, elem in enumerate(elems):
        nxt: int = pos + 1
        if nxt < len(elems):
            succ: Elem = elems[nxt]
            text: str = f"What comes after: {elem.text}\n---\n{succ.text}"
            cards.append(Card(text=text))
    return cards


def make_predecessor(elems: list[Elem]) -> list[Card]:
    cards: list[Card] = []
    for pos, elem in enumerate(elems):
        prev: int = pos - 1
        if prev >= 0:
            succ: Elem = elems[prev]
            text: str = f"What comes before: {elem.text}\n---\n{succ.text}"
            cards.append(Card(text=text))
    return cards


# Entrypoint.

if __name__ == "__main__":
    main()
