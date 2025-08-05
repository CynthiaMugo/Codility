// Given a string, find the first character that does not repeat anywhere in the string. Return None if all characters repeat.
// Input: "Hello"
// Output: "H"
// Input: "Swiss"
// Output: "w"
function firstNonRepeatCharacter(string) {
    const charCount = {};

    for (let char of string) {
        if (charCount[char]) {
            charCount[char] += 1;
        } else {
            charCount[char] = 1;
        }
        }

    for (let char of string) {
        if (charCount[char] === 1) {
        return char;
        }
    }
    return null;
}
console.log(firstNonRepeatCharacter("Hello"));
console.log(firstNonRepeatCharacter("Swiss"))