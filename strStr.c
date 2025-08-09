#include <string.h>
int strStr(char* haystack, char* needle) {
        // Handle edge cases where either string is NULL or empty
    if (!haystack || !needle) {
        return -1; // Or handle as per specific requirements, e.g., return 0 if needle is empty
    }

    int len_haystack = strlen(haystack);
    int len_needle = strlen(needle);

    // If needle is an empty string, return 0 (as it's considered found at the beginning)
    if (len_needle == 0) {
        return 0;
    }

    // If needle is longer than haystack, it cannot be found
    if (len_needle > len_haystack) {
        return -1;
    }

    // Iterate through the haystack
    for (int i = 0; i <= len_haystack - len_needle; i++) {
        // Check if the substring of haystack starting at 'i' matches needle
        int j;
        for (j = 0; j < len_needle; j++) {
            if (haystack[i + j] != needle[j]) {
                break; // Mismatch found, move to the next starting position in haystack
            }
        }
        // If the inner loop completed, it means a match was found
        if (j == len_needle) {
            return i; // Return the starting index of the match
        }
    }

    // If no match is found after checking all possibilities
    return -1;


}
