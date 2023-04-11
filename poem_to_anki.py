#!/usr/bin/python3
import sys
import csv

def read_poem_from_stdin():
    poem = []
    for line in sys.stdin:
        poem.append(line.strip())
    return poem

def convert_poem_to_anki_flashcards(poem):
    flashcards = []
    title_and_author = f"{poem[0]} by {poem[1]}"
    flashcards.append([f"<i>Beginning</i>", poem[2]])

    flashcards.append([f"<i>Beginning</i><br>{poem[2]}", poem[3]])

    for i in range(4, len(poem)):
        flashcards.append([f"{poem[i - 2]}<br>{poem[i - 1]}", poem[i]])

    return flashcards

def output_flashcards_to_stdout(flashcards):
    csv_writer = csv.writer(sys.stdout, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for flashcard in flashcards:
        csv_writer.writerow(flashcard)

def main():
    poem = read_poem_from_stdin()
    flashcards = convert_poem_to_anki_flashcards(poem)
    output_flashcards_to_stdout(flashcards)

if __name__ == "__main__":
    main()

