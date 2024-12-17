function maxScore(cardPoints: number[], k: number): number {
    let n = cardPoints.length; // Get the length of the cardPoints array
    let currentSum = 0; // Initialize currentSum to store the sum of the first k cards

    // Calculate the sum of the first k cards (initial sliding window)
    for (let i = 0; i < k; i++) {
        currentSum += cardPoints[i];
    }

    let maxNum = currentSum; // Initialize maxNum to the sum of the first k cards

    // Use a sliding window to replace cards from the beginning with cards from the end
    for (let i = 0; i < k; i++) {
        // Update currentSum by removing the card from the beginning and adding the card from the end
        currentSum = (currentSum - cardPoints[k - 1 - i]) + cardPoints[n - 1 - i];
        // Update maxNum if the new currentSum is greater
        maxNum = currentSum > maxNum ? currentSum : maxNum;
    }

    return maxNum; // Return the maximum sum of k card
    
};
