function toBase62(deci) {
    const s = '012345689abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let hashStr = '';
    while (deci > 0) {
        hashStr = s[Math.floor(deci % 62)] + hashStr;
        deci = Math.floor(deci / 62);
    }
    return hashStr;
}

