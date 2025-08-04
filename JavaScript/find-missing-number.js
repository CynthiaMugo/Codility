function findMissingNumber(numbers) {
    const n = numbers.length
    for (let i = 0; i < n; i = i + 1) {
        if (!numbers.includes(i)) {
            return i;
        }
    }
}
console.log(findMissingNumber([3, 0, 1]))