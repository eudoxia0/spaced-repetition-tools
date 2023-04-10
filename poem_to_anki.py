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
    flashcards.append([f"Beginning of {title_and_author}", poem[2]])

    for i in range(3, len(poem)):
        new_line = '\n\n'
        flashcards.append([f"# {title_and_author} {new_line} {poem[i - 1]}", poem[i]])

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

