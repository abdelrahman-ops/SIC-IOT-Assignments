function findMinMax(arr) {
    if (arr.length === 0) {
      return { min: undefined, max: undefined };
    }
  
    let min = arr[0];
    let max = arr[0];
  
    for (let i = 1; i < arr.length; i++) {
      if (arr[i] < min) {
        min = arr[i];
      }
      if (arr[i] > max) {
        max = arr[i];
      }
    }
  
    return { min, max };
}

const numbers = [5, 2, 9, 1, 5, 6];
const result = findMinMax(numbers);

console.log(`Minimum: ${result.min}`);
console.log(`Maximum: ${result.max}`);

  