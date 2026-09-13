# Step 3: Document and Reflect on the Results

### Student:    Kindy Amarachi Paito
### Lab:        00
### Course:     AI for Programmer

#### 1. Languages and Tools

  **a. The familiar language used in Step 1.**
  - JavaScript

  **b. The unfamiliar language used in Step 2.**
  - Python 3

  **c. The AI/LLM used in Step 2.**
   - Gemini

#### 2. Manual Implementation

**a. Your complete Step 1 code.**
  
      let summarizeRanges = values;
          for(let i = 0; i < values.length; i++) {
          function summarizeRanges(values) {  
          }
          // Lists
          console.log(summarizeRanges([]));                       // Expected: "none"
          console.log(summarizeRanges([7]));                      // Expected: "7"
          console.log(summarizeRanges([1, 2, 3, 4, 5]));          // Expected: "1-5"
          console.log(summarizeRanges([1, 3, 5, 7]));             // Expected: "1, 3, 5, 7"
          console.log(summarizeRanges([1, 2, 3, 5, 7, 8, 9]));    // Expected: "1-3, 5, 7-9"
          console.log(summarizeRanges([0, 1, 2, 6, 7, 10]));      // Expected: "0-2, 6-7, 10"
          console.log(summarizeRanges([98, 99, 100]));            // Expected: "98-100"
          console.log(summarizeRanges([2, 4, 5, 6, 9, 11, 12]));  // Expected: "2, 4-6, 9, 11-12"
      return TimeRanges(" , ");
      }

**b. Your test cases and results.**
  - Tested in Visual Studio code
  - All test cases matched required output specifications (none, 7, 1-5, 1, 3, 5, 7, 1-3, 5, 7-9, 0-2, 6-7, 10).

**c. The total time required.**
  -  1 hour

**d. A short description of your approach.**
   - A single loop was used to inspect contiguous indices.
   - Identified range boundaries whenever the next element was not current + 1 or when reaching the array's end.

**e. Any bugs or challenges you encountered.**
  - None


#### 3. AI-Assisted Implementation

**a. Your complete Step 2 code.**

      def summarize_ranges(values):
          # Return "none" if the list is empty
          if len(values) == 0:
              return "none"
          ranges = []
          i = 0
          while i < len(values):
              start = values[i]
              # Keep moving forward as long as numbers are consecutive
              while i + 1 < len(values) and values[i + 1] == values[i] + 1:
                  i += 1
              end = values[i]
              # Format as single numbere
              if start == end:
                  ranges.append(str(start))
              else:
                  ranges.append(str(start) + "-" + str(end))
              i += 1
          # Join items with comma and space
          return ", ".join(ranges)
      print(summarize_ranges([]))  # Expected: "none"
      print(summarize_ranges([7]))  # Expected: "7"
      print(summarize_ranges([1, 2, 3, 4, 5]))  # Expected: "1-5"
      print(summarize_ranges([1, 3, 5, 7]))  # Expected: "1, 3, 5, 7"
      print(summarize_ranges([1, 2, 3, 5, 7, 8, 9]))  # Expected: "1-3, 5, 7-9"
      print(summarize_ranges([0, 1, 2, 6, 7, 10]))  # Expected: "0-2, 6-7, 10"
      print(summarize_ranges([98, 99, 100]))  # Expected: "98-100"
      print(summarize_ranges([2, 4, 5, 6, 9, 11, 12]))  # Expected: "2, 4-6, 9, 11-12"

**b. Your test cases and results.**
  -  Executed in Spyder IDE (step02PartBnC.py). 
  - Outputs verified in the console: none, 7, 1-5, 1, 3, 5, 7, 1-3, 5, 7-9, 0-2, 6-7, 10, 98-100, 2, 4-6, 9, 11-12.

**c. The total time required.**
   - 1hour, 5 minutes

**d. Two or three important prompts you gave the LLM.**
   - Port this working JavaScript function to Python 3. Follow the exact logic, and explain to me how Python handles lists, loops, conditional checks, and string joining compared to JavaScript.
    - Make the Python code easy to understand and concise for a beginner.

**e. Any incorrect code or instructions produced by the LLM.**
   - The initial generated port used C-style indexing inside a single for loop. 
    - While functional, it was harder to read, so I prompted the LLM to refactor it into an intuitive while loop structure.

**f. A brief explanation of how you verified the final solution.**
   - Run and Debug in Spyder IDE
   - Verified output to see if run - and it run successfully

#### 4. Reflection

**a. Time and Effort**
    - AI felt easier and faster.
    - Why: i don't have to think a lot as the code was generated using prompts, then reviewed the code.

**b. AI's Strongest Role**
   - Explaining unfamiliar language features and logics.

**c. AI's Weakest Role**
   - Initial prompts generated complex code range.
   - Inputted another prompt asking for a clean, beginner-friendly Python code and logics

**d. Verification**
  - How did you determine that the AI-generated program was correct?
  
    - I run them on the IDE, and if their is no error, showing is accurate

  - Did all of the provided examples pass?

     - Yes
    
   - Did you add any tests of your own?
     - I only added the test : print("Hello World!)

**e. Impact on Learning**
  - Learned Pythin starts with the header : def summarize_ranges(values)
  - Unlike JavaScript that uses "console()", Python uses "print()"

**f. Preferred Workflow**
  - Part I would complete myself : JavaScript 50%
  - Part 2 would complete with LLM help : Python anduse a bit of LLM with JavaScript
