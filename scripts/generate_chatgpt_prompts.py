import json

task_descriptions = {
    1: "Summarize the functionality of the following Java method that counts word frequencies in a list.",
    2: "Identify and fix the off-by-one error in the following Python function.",
    3: "Classify the bug in this C++ function that returns a pointer to a local variable.",
    4: "Complete the following Python function using a regex pattern to validate basic email addresses.",
    5: "Implement a Flask API endpoint that returns a greeting based on the provided username.",
    6: "Design a SQL schema for a review app involving users, books, and reviews.",
    7: "Identify the null dereference risk in the following Java method and suggest a fix.",
    8: "Improve the given CSV parser to handle quoted fields properly.",
    9: "Convert the following Kotlin data class into a REST API using Ktor, with GET and POST endpoints.",
    10: "Write a brief summary of what this Python function does with a sentence as input.",
    11: "Write a prompt that could generate the following prime-checking Python function based on its comment.",
    12: "Fix the factorial function to handle input 0 correctly.",
    13: "Implement the missing logic in this C function to delete a node from a linked list by its value.",
    14: "Complete the recursive Fibonacci function in Python with proper base cases and recursive logic.",
    15: "Finish the Python class constructor by adding name, age, and an optional email field.",
    16: "Finish the binary search implementation in Java by comparing and adjusting the search bounds.",
    17: "Resolve the inconsistency between this C++ function's name and its logic.",
    18: "Identify the bug in the JavaScript function and fix it so it returns a proper boolean value.",
    19: "Break down the logic of this C++ function based on the provided high-level comment.",
    20: "Complete this Python function to return the average of a list of scores.",
    21: "Analyze the Python utility script for logic or design flaws, and refactor it for better readability and safety.",
    22: "Complete this Python file-processing script to clean punctuation and count word frequencies robustly."
}

task_code_snippets = {
    1: '''public Map<String, Integer> countWordFrequency(List<String> words) {
    Map<String, Integer> freqMap = new HashMap<>();
    for (String word : words) {
        freqMap.put(word, freqMap.getOrDefault(word, 0) + 1);
    }
    return freqMap;
}''',
    2: '''def sum_range(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total''',
    3: '''int* getArray(int size) {
    int arr[size]; // Warning: local array
    return arr;    // Bug: returning pointer to local variable
}''',
    4: '''def is_valid_email(email):
    # TODO: Complete using regex
    pass''',
    5: '''from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/greet/<username>')
def greet(username):
    # TODO: Return a JSON greeting
    pass''',
    6: '''-- Tables: users(id, name), books(id, title), reviews(id, user_id, book_id, rating)
-- TODO: Design schema with appropriate keys and constraints''',
    7: '''public int getLength(String s) {
    return s.length(); // What if s is null?
}''',
    8: '''def parse_csv_line(line):
    return line.split(',')  # Incomplete: doesn't handle quoted fields''',
    9: '''data class Product(val id: Int, val name: String, val price: Double)
// TODO: Create GET and POST endpoints using Ktor''',
    10: '''def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])''',
    11: '''# This function checks if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True''',
    12: '''def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result''',
    13: '''struct Node {
    int data;
    struct Node* next;
};
void deleteNode(struct Node** head, int key) {
    // TODO: Implement node deletion
}''',
    14: '''def fibonacci(n):
    # TODO: Base cases and recursive call
    pass''',
    15: '''class Person:
    def __init__(self):
        # TODO: Add name, age, and optional email
        pass''',
    16: '''public int binarySearch(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        // TODO: Compare and adjust bounds
    }
    return -1;
}''',
    17: '''// Supposed to return true if x is even
bool isOdd(int x) {
    return x % 2 == 0; // Logic contradicts function name
}''',
    18: '''function isEven(n) {
    return n % 2; // Returns 1 or 0, not true/false
}''',
    19: '''// Function that validates input, calculates square, and returns result
int process(int x) {
    if (x < 0) return -1;
    return x * x;
}''',
    20: '''def calculate_average(scores):
    total = 0
    # TODO: Complete to return average
    pass''',
    21: '''import csv
def read_csv(filepath):
    with open(filepath, 'r') as f:
        return [row for row in csv.reader(f)]

def summarize_column(data, index):
    values = [float(row[index]) for row in data[1:]]  # skip header
    total = sum(values)
    avg = total / len(values)
    return total, avg

def main():
    filepath = 'data.csv'
    data = read_csv(filepath)
    total, avg = summarize_column(data, 1)
    print("Total:", total)
    print("Average:", avg)

if __name__ == '__main__':
    main()''',
    22: '''import string
def load_file(filepath):
    with open(filepath, 'r') as f:
        return f.readlines()

def clean_line(line):
    # TODO: Remove punctuation and make lowercase
    pass

def count_words(lines):
    word_counts = {}
    for line in lines:
        clean = clean_line(line)
        for word in clean.split():
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def main():
    filepath = 'input.txt'
    lines = load_file(filepath)
    counts = count_words(lines)
    for word, count in sorted(counts.items()):
        print(f"{word}: {count}")

if __name__ == '__main__':
    main()'''
}

# Rebuild the prompt list
full_prompts_with_code = []

for i in range(1, 23):
    code = task_code_snippets[i]
    desc = task_descriptions[i]
    zs_prompt = f"{desc}\n\n`{code}`"
    fs_prompt = f"Example:\nInput: [example input related to task {i}]\nOutput: [expected output]\n\n{desc}\n\n`{code}`"

    full_prompts_with_code.append({
        "task_number": i,
        "strategy": "zero-shot",
        "prompt": zs_prompt
    })
    full_prompts_with_code.append({
        "task_number": i,
        "strategy": "few-shot",
        "prompt": fs_prompt
    })

# Save final file
final_output_path = "gpt4_prompts.json"
with open(final_output_path, "w") as f:
    json.dump(full_prompts_with_code, f, indent=2)

print(f"Prompts saved to {final_output_path}")
