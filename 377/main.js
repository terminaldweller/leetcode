#!/home/devi/.bun/bin/bun

var combinationSum4 = function (nums, target, memo = {}) {
  let sum = 0;
  if (target in memo) {
    return sum + memo[target];
  }
  if (target === 0) {
    sum++;
    return sum;
  }
  if (target < 0) {
    return sum;
  }

  for (let num of nums) {
    var remainder = target - num;
    if (remainder === 0) {
      sum++;
      if (remainder in memo) {
        memo[remainder]++;
      } else {
        memo[remainder] = 1;
      }
    }
    if (remainder > 0) {
      memo[remainder] = combinationSum4(nums, remainder, memo);
      sum += memo[remainder];
    }
  }

  console.log(memo);
  memo[target] = sum;
  return sum;
};

console.log(combinationSum4([1, 2, 3], 4));
console.log(combinationSum4([4, 2, 1], 32));
