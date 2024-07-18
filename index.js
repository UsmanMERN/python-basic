// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

const sumOfTwo = (nums, target) => {
    let first_num = nums[0]
    for (number in nums) {
        let sum = first_num + nums[number]
        // console.log('number', nums[number])
    }
}

sumOfTwo([2, 7, 11, 15], 9)
