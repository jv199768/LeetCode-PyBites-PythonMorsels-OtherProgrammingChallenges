















/**
 * Calculate the sum of distances between each node and all other nodes in a tree
 * @param n - Number of nodes in the tree
 * @param edges - Array of edges representing connections between nodes
 * @returns Array where ans[i] is the sum of distances from node i to all other nodes
 */
function sumOfDistancesInTree(n: number, edges: number[][]): number[] {
    // Build adjacency list representation of the tree
    const adjacencyList: number[][] = Array.from({ length: n }, () => []);
    for (const [nodeA, nodeB] of edges) {
        adjacencyList[nodeA].push(nodeB);
        adjacencyList[nodeB].push(nodeA);
    }
  
    // Array to store the sum of distances for each node
    const distanceSums: number[] = new Array(n).fill(0);
  
    // Array to store the size of subtree rooted at each node
    const subtreeSizes: number[] = new Array(n).fill(0);
  
    /**
     * First DFS: Calculate the sum of distances from root (node 0) to all other nodes
     * and compute the size of each subtree
     * @param currentNode - Current node being visited
     * @param parent - Parent of the current node (-1 for root)
     * @param depth - Current depth from the root
     */
    const calculateRootDistanceAndSubtreeSizes = (
        currentNode: number, 
        parent: number, 
        depth: number
    ): void => {
        // Add current depth to the total distance sum for root
        distanceSums[0] += depth;
      
        // Initialize subtree size for current node
        subtreeSizes[currentNode] = 1;
      
        // Visit all neighbors except parent
        for (const neighbor of adjacencyList[currentNode]) {
            if (neighbor !== parent) {
                calculateRootDistanceAndSubtreeSizes(neighbor, currentNode, depth + 1);
                // Add size of child's subtree to current node's subtree size
                subtreeSizes[currentNode] += subtreeSizes[neighbor];
            }
        }
    };
  
    /**
     * Second DFS: Calculate the sum of distances for all other nodes using rerooting technique
     * When moving from parent to child, nodes in child's subtree get closer by 1,
     * while all other nodes get farther by 1
     * @param currentNode - Current node being visited
     * @param parent - Parent of the current node
     * @param parentDistanceSum - Sum of distances for the parent node
     */
    const calculateAllDistanceSums = (
        currentNode: number, 
        parent: number, 
        parentDistanceSum: number
    ): void => {
        // Set the distance sum for current node
        distanceSums[currentNode] = parentDistanceSum;
      
        // Visit all neighbors except parent
        for (const neighbor of adjacencyList[currentNode]) {
            if (neighbor !== parent) {
                // When moving from currentNode to neighbor:
                // - subtreeSizes[neighbor] nodes get closer by 1 (subtract subtreeSizes[neighbor])
                // - (n - subtreeSizes[neighbor]) nodes get farther by 1 (add n - subtreeSizes[neighbor])
                // Total change: -subtreeSizes[neighbor] + (n - subtreeSizes[neighbor]) = n - 2 * subtreeSizes[neighbor]
                const neighborDistanceSum = parentDistanceSum - subtreeSizes[neighbor] + (n - subtreeSizes[neighbor]);
                calculateAllDistanceSums(neighbor, currentNode, neighborDistanceSum);
            }
        }
    };
  
    // First pass: Calculate distances from root and subtree sizes
    calculateRootDistanceAndSubtreeSizes(0, -1, 0);
  
    // Second pass: Calculate distances for all nodes using rerooting
    calculateAllDistanceSums(0, -1, distanceSums[0]);
  
    return distanceSums;
}
