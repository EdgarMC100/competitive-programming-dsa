# Bubble Sort

A visual and algorithmic breakdown of **Bubble Sort**, focusing on index logic, pass tracking, and loop optimizations.

## 🧠 Core Concept

Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

## 📉 Optimization: Reducing Redundant Checks

Without optimization, the inner loop always checks all elements. By tracking outer passes ($i$), we know that the last $i$ elements are already sorted.

* **Inner Loop Condition:** `j < N - i - 1`
* **Why the `- 1`?** Prevents index out-of-bounds errors when comparing `array[j]` with `array[j + 1]`.
* **Why the `-i`?** Skips the tail elements that are already locked in their final sorted positions.

## ▶️ How to Run

Each implementation is a self-contained script with a built-in example array.

### Python — `bubble_sort.py`

```bash
python3 bubble_sort.py
```

### JavaScript — `bubble_sort.js`

```bash
node bubble_sort.js
```

### TypeScript — `bubble_sort.ts`

```bash
ts-node bubble_sort.ts
```

> Requires `ts-node` (`npm install -g ts-node`). Alternatively, with `npx tsx bubble_sort.ts` or `bun bubble_sort.ts`.

## 🖼️ Visual Trace & Flowchart

* **Flowchart:** [View Flowchart](./flowchart.png)
* **Step-by-step Trace:** [View Trace Sheet](./trace-sheet.png)
