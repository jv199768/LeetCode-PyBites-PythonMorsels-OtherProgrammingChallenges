int myAtoi(char* s) {
    int sign = 1, base = 0, i = 0;
 
    // if whitespaces then ignore.
    while (s[i] == ' ') {
        i++;
    }
 
    // sign of number
    if (s[i] == '-' || s[i] == '+') {
        sign = 1 - 2 * (s[i++] == '-');
    }
 
    // checking for valid input
    while (s[i] >= '0' && s[i] <= '9') {
        // handling overflow test case
        if (base > INT_MAX / 10
            || (base == INT_MAX / 10 && s[i] - '0' > 7)) {
            if (sign == 1)
                return INT_MAX;
            else
                return INT_MIN;
        }
        base = 10 * base + (s[i++] - '0');
    }
    return base * sign;
}
