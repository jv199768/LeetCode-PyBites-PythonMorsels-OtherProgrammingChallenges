let bytesToProcess: number = 0;

function validUtf8(data: number[]): boolean {
    bytesToProcess = 0;
        for (let currentValue of data) {
        if (bytesToProcess > 0) {
            // Check if the current byte is a continuation byte (should start with bits 10xxxxxx).
            if ((currentValue >> 6) !== 0b10) {
                return false; // If not, the sequence is invalid, return false.
            }
            bytesToProcess--; // Decrease the count for bytes left to process.
        } else {
            // Determine the number of bytes in the current UTF-8 character based on its first byte value.
            if ((currentValue >> 7) === 0b0) {
                bytesToProcess = 0; // Single-byte character (0xxxxxxx).
            } else if ((currentValue >> 5) === 0b110) {
                bytesToProcess = 1; // Two-byte character (110xxxxx 10xxxxxx).
            } else if ((currentValue >> 4) === 0b1110) {
                bytesToProcess = 2; // Three-byte character (1110xxxx 10xxxxxx 10xxxxxx).
            } else if ((currentValue >> 3) === 0b11110) {
                bytesToProcess = 3; // Four-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx).
            } else {
                return false; // If the pattern is not valid for UTF-8, return false.
            }
        }
    }

    return bytesToProcess === 0;
    
};
