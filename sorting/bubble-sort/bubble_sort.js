function bubble_sort(numbers) {
    let n = numbers.length;
    for (let i = 0; i < n - 1; i++) {
        console.log(`i:${i}`);
        let swapped = false;
        for (let j = 0; j < n - i - 1; j++) {
            console.log(`j${j} -> ${numbers[j]}, j+1 -> ${numbers[j + 1]} `, numbers);
            if (numbers[j] > numbers[j + 1]) {
                [numbers[j], numbers[j + 1]] = [numbers[j + 1], numbers[j]];
                swapped = true;
                console.log("Swapped positions");
            }
        }
        if (!swapped) {
            break;
        }
    }
    return numbers;
}

console.log(bubble_sort([5, 3, 7, 10, 1]));
