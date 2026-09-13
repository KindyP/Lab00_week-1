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
