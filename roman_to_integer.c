inline int table(char c){
    if(c=='I') return 1;
    if (c=='V') return 5;
    if (c== 'X') return 10;
    if(c == 'L') return 50;
    if(c == 'C') return 100;
    if(c == 'D') return 1000;
    else return 0;
}
int romanToInt(char* s) {
    int res = 0;
    char curr, next;
    while (*s){
        curr = *s;
        next = *(s+1);
        if(table(curr) < table(next))
            res -= table(curr);
        else
            res += table(curr);
        s++;
    }

    return res;
    
}
