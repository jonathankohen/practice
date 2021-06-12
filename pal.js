let string = 'racecar';

const pal = str => {
    return str.split('').reverse().join('') == str;
};

const longestPal = s => {
    let counter = 0;

    for (const i of s) {
        console.log(s.slice(i, s.length - counter));
        counter++;
    }
};

console.log(longestPal(string));
