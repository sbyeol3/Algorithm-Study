function solution(numbers) {
    const unsorted = numbers.reduce((prev, num, idx) => {
        const sub = numbers.slice(idx+1).reduce((prev, subNum) => {
            return [...prev, num + subNum];
        }, []);
        return prev.concat(sub);
    }, []);
    const set = new Set(unsorted);
    return [...set].sort((a,b) => {return a-b;});
}