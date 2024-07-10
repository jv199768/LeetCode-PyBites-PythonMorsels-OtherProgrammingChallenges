/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
   
    // If the array length does not match the given dimensions, return an empty array
    if (rowsCount * colsCount !== this.length) {
      return [];
    }

    // Initialize the answer array with zeros and the specified number of rows and columns
    const answer = Array.from({ length: rowsCount }, () => Array(colsCount).fill(0));

    let elementIndex = 0;
    let rowIndex = 0;
    let colIndex = 0;
    let direction = 1;

    // Loop through the array to assign each element to the answer matrix
    while (elementIndex < this.length) {
      // Assign the current element to the current position in the answer array
      answer[rowIndex][colIndex] = this[elementIndex];
      elementIndex++;

      // Update the rowIndex according to the current direction (up or down)
      rowIndex += direction;

      // Check and handle boundaries for row and column indices
      if (rowIndex === rowsCount || rowIndex === -1) {
        // If out of bounds, reverse the direction (up becomes down, and vice-versa)
        rowIndex -= direction;
        direction = -direction;

        // Move to the next column since we've reached the end or beginning of a row
        colIndex++;
      }
    }

    return answer;
  
    
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */
