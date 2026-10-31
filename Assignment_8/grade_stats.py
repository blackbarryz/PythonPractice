from pathlib import Path

GRADES_FILE = Path(__file__).resolve().parent / "grades.csv"

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2


def main():
    """Read the grades file, compute each student's weighted final
    grade, and print a summary of how many students fall into each
    grade range."""
    weighted_grades = []
    
    try:
        # Open and read all lines from the CSV file
        with open(GRADES_FILE, 'r') as csv_file:
            lines = csv_file.readlines()
            
        # Verify the file is not empty and skip the header row
        if len(lines) > 1:
            for line in lines[1:]:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue  # Safely skip trailing empty lines
                
                # Process the row to get the student's weighted final grade
                final_grade = process_row(cleaned_line)
                weighted_grades.append(final_grade)
                
            # Analyze and print the distribution summary
            analyze_grade(weighted_grades)
        else:
            print("Error: The grades file is empty or missing data rows.")
            
    except FileNotFoundError:
        print(f"Error: Could not find the file at {GRADES_FILE}")
    except (ValueError, IndexError) as e:
        print(f"Error processing grade records: {e}")


def process_row(row):
    """Given one row from the grades file, return that student's
    weighted final grade (bypass the Name and StudentID columns)."""
    # Tokenize the comma-separated string row into a list
    tokens = row.split(',')
    
    # Slice the respective tokens and convert them to numeric values
    # Format: Name (0), StudentID (1), 4 Tests (2:6), 2 Exams (6:8), 2 Discussions (8:10), Project (10)
    test_scores = [float(score) for score in tokens[2:6]]
    exam_scores = [float(score) for score in tokens[6:8]]
    discussion_scores = [float(score) for score in tokens[8:10]]
    project_score = float(tokens[10])
    
    # Calculate subject averages using the helper function
    test_avg = average_subject(test_scores)
    exam_avg = average_subject(exam_scores)
    discussion_avg = average_subject(discussion_scores)
    
    # Compute and return the aggregated final weight calculation
    return weight_final(test_avg, exam_avg, discussion_avg, project_score)


def average_subject(subject_list):
    """Return the average of the scores in subject_list."""
    if not subject_list:
        return 0.0
    return sum(subject_list) / len(subject_list)


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    """Return a student's weighted final grade, combining the test,
    exam, discussion, and project scores using the weight constants
    declared above."""
    weighted_score = (test_avg * TEST_WEIGHT) + \
                     (exam_avg * EXAM_WEIGHT) + \
                     (discussion_avg * DISCUSSION_WEIGHT) + \
                     (project_score * PROJECT_WEIGHT)
    return weighted_score


def analyze_grade(weight_final_list):
    """Count and print how many students fall into each grade range:
    90 or above, 80-89, 70-79, 60-69, and below 60."""
    # Initialize count tracking buckets
    count_90_above = 0
    count_80_89 = 0
    count_70_79 = 0
    count_60_69 = 0
    count_below_60 = 0
    
    # Categorize every final grade item in the sequence list
    for grade in weight_final_list:
        if grade >= 90:
            count_90_above += 1
        elif grade >= 80:
            count_80_89 += 1
        elif grade >= 70:
            count_70_79 += 1
        elif grade >= 60:
            count_60_69 += 1
        else:
            count_below_60 += 1
            
    # Print the exact matching string layout from the required output
    print(f"Number of students with final grade 90 or above: {count_90_above}")
    print(f"Number of students with final grade 80–89: {count_80_89}")
    print(f"Number of students with final grade 70–79: {count_70_79}")
    print(f"Number of students with final grade 60–69: {count_60_69}")
    print(f"Number of students with final grade below 60: {count_below_60}")


if __name__ == "__main__":
    main()
