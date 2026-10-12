impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        
        let mut memo = vec![-1; nums.len()];
        fn dfs(nums: &[i32], i: usize, memo: &mut Vec<i32>)->i32 {
            if i >=nums.len(){
                return 0;
            }
            if memo[i]!=-1{
                return memo[i];
            }
            memo[i] = dfs(nums,i+1,memo).max(nums[i]+dfs(nums,i+2,memo));
            memo[i]

        }
        dfs(&nums, 0,&mut memo)


    }
}
