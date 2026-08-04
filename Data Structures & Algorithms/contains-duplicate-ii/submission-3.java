class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashSet<Integer> s = new HashSet<>();
        int l = 0;

        for (int i = 0; i < nums.length; i++) {
            if (i - l > k) {
                s.remove(nums[l]);
                l++;
            }

            if (s.contains(nums[i])) {
                return true;
            }
            s.add(nums[i]);
        }
        return false;
    }
}