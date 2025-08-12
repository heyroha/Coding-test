function solution(n, k) {
    var answer = 0;
    const freeCan = Math.floor(n/10);
    answer = (12000 * n + 2000 * (k-freeCan));
    return answer;
}