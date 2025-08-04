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