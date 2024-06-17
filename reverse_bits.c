#define LSB_bitmask (uint32_t) 1
#define MSB_bitmask 0x80000000
uint32_t reverseBits(uint32_t n) {
    uint32_t result = 0,left_pointer, right_pointer; 
    short i, index;
    for( i = 0, index=31; i < 16; i++, index--){
        // Extract Bits using two running pointers
        right_pointer = n & (LSB_bitmask << i);
        left_pointer = n & (MSB_bitmask >> i);
        //printf("Before Swap i:%i, left: %x right:%x\n", i,left_pointer, right_pointer);
        // Move the left pointer to its corresponding reverse position to the right
        left_pointer = left_pointer>>index-i; // shift operation with indices
        // Move the right pointer to its corresponding reverse position to the left
        right_pointer = right_pointer<<index-i;// shift operation with indices
        // Update result
        result |= left_pointer|right_pointer;
        //printf("After Swap: left: %x right:%x result: %x\n", left_pointer, right_pointer, result);
    }
    return result ;
}
