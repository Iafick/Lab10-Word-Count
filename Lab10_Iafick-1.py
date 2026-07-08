"""
Program Name: Word Count Analyzer
Author: Imran Afick
Purpose:This program demonstrates Object-Oriented Programming by creating a
        WordAnalyzer class that reads text files, counts word frequencies,
        and displays an alphabetical report.
Starter Code: None
Date:
July 7, 2026
"""

from pathlib import Path
import string


class WordAnalyzer:
    
   #  Handles reading a file and analyzing word frequency.

    def __init__(self, filepath):
        # Private Path object
        self.__filepath = Path(filepath)

        # Private dictionary for word counts
        self.__frequencies = {}


    def process_file(self):
        
       # this Reads file and counts words.
       #Returns True if successful, False otherwise.
        

        try:

            # Check if file exists
            if not self.__filepath.exists():
                raise FileNotFoundError


            # Create translation table to remove punctuation
            translator = str.maketrans("", "", string.punctuation)


            # Open and read file line by line
            with self.__filepath.open("r", encoding="utf-8") as file:

                for line in file:

                    # Remove punctuation
                    line = line.translate(translator)

                    # Convert lowercase
                    line = line.lower()

                    # Split into words
                    words = line.split()


                    # Count words
                    for word in words:

                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1


            return True


        except FileNotFoundError:

            print("Error: File not found.")
            return False



    def print_report(self):
        """
        Prints alphabetical word count report.
        """

        print()

        # Sort dictionary keys alphabetically
        sorted_words = sorted(self.__frequencies.keys())


        for word in sorted_words:
            print(f"{word:<10} :: {self.__frequencies[word]}")



def main():

    # Dictionary containing files
    files = {
        "1": Path("moby_dick_ch1.txt"),
        "2": Path("frankenstein_ch1.txt"),
        "3": Path("alice_ch1.txt"),
        "4": Path("pride_prejudice_ch1.txt")
    }


    names = {
        "1": "Moby Dick (Chapter 1)",
        "2": "Frankenstein (Chapter 1)",
        "3": "Alice in Wonderland (Chapter 1)",
        "4": "Pride and Prejudice (Chapter 1)"
    }



    while True:

        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")

        for key in names:
            print(f"{key}. {names[key]}")

        print("5. Exit")


        choice = input("\nEnter your choice (1-5): ")



        if choice == "5":
            print("\nGoodbye!")
            break



        elif choice in files:

            filename = files[choice]


            print(f"\nProcessing '{filename}'...")


            analyzer = WordAnalyzer(filename)


            success = analyzer.process_file()


            if success:
                analyzer.print_report()


            input("\nPress Enter to return to the menu...")



        else:

            print("\nInvalid choice. Please select from 1-5.")

            input("\nPress Enter to return to the menu...")



if __name__ == "__main__":
    main()