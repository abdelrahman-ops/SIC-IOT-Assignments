function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }

    const middle = Math.floor(arr.length / 2);
    const leftHalf = arr.slice(0, middle);
    const rightHalf = arr.slice(middle);

    const sortedLeft = mergeSort(leftHalf);
    const sortedRight = mergeSort(rightHalf);

    return merge(sortedLeft, sortedRight);
}

function merge(left, right) 
{
    const mergedArray = [];
    let leftIndex = 0;
    let rightIndex = 0;

    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] < right[rightIndex]) {
            mergedArray.push(left[leftIndex]);
            leftIndex++;
        } else {
            mergedArray.push(right[rightIndex]);
            rightIndex++;
        }
    }

    return mergedArray.concat(left.slice(leftIndex), right.slice(rightIndex));
}

const unsortedArray = [12, 11, 13, 5, 6, 7];
const sortedArray = mergeSort(unsortedArray);

console.log("Original Array:", unsortedArray);
console.log("Sorted Array:", sortedArray);
