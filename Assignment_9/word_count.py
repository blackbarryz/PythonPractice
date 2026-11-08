# This program reads a text file and counts unique word frequencies.

def main():
    # Prompt matched to screenshot 2
    filename = input("Enter the name of the input file: ").strip()
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Split purely on whitespace matching the textbook scope
            words_list = content.split()
            
        # Filter duplicates using a set object
        unique_words = set(words_list)
        
        # Initialize and build counts
        word_counts = {}
        for word in unique_words:
            word_counts[word] = 0
            
        for word in words_list:
            if word in word_counts:
                word_counts[word] += 1
                
        # Tabular header layout
        print(f"{'Word':<15} {'Occurrences':<10}")
        print("-" * 50)
        
        for word, count in word_counts.items():
            print(f"{word:<15} {count:<10}")
            
    except FileNotFoundError:
        print(f"Error: Could not find file named '{filename}'.")

if __name__ == '__main__':
    main()
