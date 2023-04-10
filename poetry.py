#!/usr/bin/env python
from dataclasses import dataclass
import sys
import csv

@dataclass(frozen=True)
class Line:
    # The line's position in the poem, zero-indexed.
    index: int
    # The text of the poem's line.
    text: str

    def __post_init__(self):
        assert self.index >= 0

@dataclass(frozen=True)
class Card:
    context1: str
    context2: str
    line: str

def main():
    # Read all lines in the input.
    lines: list[str] = [line.strip() for line in sys.stdin.readlines()]
    # The title is the first line.
    title: str = lines[0].strip()
    # The author is the second line.
    author: str = lines[1].strip()
    # All subsequent lines are the poem.
    poem: list[Line] =  [
        Line(index=index, text=text)
        for index, text in enumerate(lines[2:])
    ]
    # Make the cards.
    cards: list[Card] = [make_card(line, poem) for line in poem]
    # Render cards.
    writer = csv.writer(
        sys.stdout,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator="\n",
    )
    for card in cards:
        writer.writerow([render_card(title, author, card)])

def make_card(line: Line, all_lines: list[Line]) -> Card:
    context1: str
    context2: str
    if line.index == 0:
        # First line of the poem.
        context1 = ""
        context2 = "_Beginning_"
    elif line.index == 1:
        # Second line of the poem.
        context1 = "_Beginning_"
        context2 = all_lines[0].text
    else:
        context1 = all_lines[line.index-2].text
        context2 = all_lines[line.index-1].text

    return Card(
        context1=context1,
        context2=context2,
        line=line.text,
    )

def render_card(title: str, author: str, card: Card) -> str:
    return f"# {title}\n{author}\n{card.context1}\n{card.context2}\n{{{{1::{card.line}}}}}"

if __name__ == "__main__":
    main()
