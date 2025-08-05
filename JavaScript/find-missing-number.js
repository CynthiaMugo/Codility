// Given a list containing n distinct numbers from 0 to n, find the missing number.
// Input: [3, 0, 1]
// Output: 2
// NOTE: No number limit
function findMissingNumber(numbers) {
    const n = numbers.length
    for (let i = 0; i < n; i = i + 1) {
        if (!numbers.includes(i)) {
            return i;
        }
    }
}
console.log(findMissingNumber([3, 0, 1]))