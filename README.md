# spaced-repetition-tools ![](https://github.com/eudoxia0/spaced-repetition-tools/actions/workflows/test.yaml/badge.svg)

This repository contains scripts for generating flashcards for import into [Mochi][mochi]. Most of these are based on [Gwern's scripts][gwern].

[mochi]: https://mochi.cards/
[gwern]: https://gwern.net/spaced-repetition

## Notes

All scripts read from stdin and write their output as a CSV to stdout.

You will want to import these into a deck with no set template, since some of the flashcards have two-sides (question-answer) and some of them have one side (cloze deletions).

## sequence.py

### Synopsis

Given a sequence, this script generates flashcards to remember that sequence. The cards are:

1. A **test card** that asks you to recall the entire sequence.
1. A **cloze card** that asks you to fill one element of the sequence.
1. For each element of the sequence:
   1. A **forward card** that asks you to recall the element from its position.
   1. A **backward card** that asks you to recall the position of a given element.
   1. A **successor card** that asks you what comes after a specific element.
   1. A **predecessor card** that asks you what comes before a specific element.

### Usage

```
cat sequence.txt | ./sequence.py > output.csv
```

### Format

The input is plain text. The first line is the title of the sequence, the subsequent lines are the elements.

### Example

Given a `greek.txt` file like this:

```
Greek Alphabet
Alpha
Beta
Gamma
```

This script will generate these flashcards:

| Question                                                | Answer              |
|---------------------------------------------------------|---------------------|
| **Greek Alphabet:** Recall all elements of the sequence | Alpha, Beta, Gamma. |
| **Greek Alphabet:** What element has position 1?        | Alpha.              |
| **Greek Alphabet:** What element has position 2?        | Beta.               |
| **Greek Alphabet:** What element has position 3?        | Gamma.              |
| **Greek Alphabet:** What is the position of Alpha?      | 1.                  |
| **Greek Alphabet:** What is the position of Beta?       | 2.                  |
| **Greek Alphabet:** What is the position of Gamma?      | 3.                  |
| **Greek Alphabet:** What comes after Alpha?             | Beta.               |
| **Greek Alphabet:** What comes after Beta?              | Gamma.              |
| **Greek Alphabet:** What comes before Beta?             | Alpha.              |
| **Greek Alphabet:** What comes before Gamma?            | Beta.               |

Plus the cloze card:

| Cloze                                                                         |
|-------------------------------------------------------------------------------|
| **Greek Alphabet:** Elements of the sequence: {{Alpha}}, {{Beta}}, {{Gamma}}. |

## poetry.py

### Synopsis

Given a poem, this script generates flashcards where you are given some context (the previous two lines) and have to recall the next line.

### Usage

```
cat poem.txt | ./poetry.py > output.csv
```

### Format

The input is plain text. The first line is the title of the sequence, the second line is the author, and subsequent lines are the poem.

### Example

Given a `wasteland.txt` file like this:

```
Archaic Torso of Apollo
Rainer Maria Rilke
We cannot know his legendary head
with eyes like ripening fruit. And yet his torso
is still suffused with brilliance from inside,
like a lamp, in which his gaze, now turned to low,
...
```

This script will generate these flashcards:

<table>
  <thead>
    <tr>
      <th>Question</th>
      <th>Answer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <i>Beginning</i><br>
        ...
      </td>
      <td>
        We cannot know his legendary head
      </td>
    </tr>
    <tr>
      <td>
        <i>Beginning</i><br>
        We cannot know his legendary head<br>
        ...
      </td>
      <td>
         with eyes like ripening fruit. And yet his torso
      </td>
    </tr>
    <tr>
      <td>
        We cannot know his legendary head<br>
        with eyes like ripening fruit. And yet his torso<br>
        ...
      </td>
      <td>
         is still suffused with brilliance from inside,
      </td>
    </tr>
    <tr>
      <td>
        with eyes like ripening fruit. And yet his torso<br>
         is still suffused with brilliance from inside,<br>
        ...
      </td>
      <td>
         like a lamp, in which his gaze, now turned to low,
      </td>
    </tr>
  </tbody>
</table>

And so on.


## Mochi Import

1. Create a new deck (don't set a template).
2. Click import, CSV, double quote as the quote character.
3. Find the output file.
4. Select the deck you just created.

## License

Copyright (c) 2023 [Fernando Borretti](https://borretti.me/).

Released under the MIT license.
