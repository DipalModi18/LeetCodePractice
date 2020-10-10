import java.util.Arrays;
import java.util.HashMap;


public class TwoSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {3, 2, 4};
		int target = 6;
		
		System.out.println(twoSum(nums, target).toString());
	}
	
	public static int[] twoSum(int[] nums, int target) {
        int val, val_index;
		HashMap<Integer, Integer> kv = new HashMap<Integer, Integer>();
		
		for(int i=0; i<nums.length; i++) {
			kv.put(nums[i], i);
		}
		
		for(int i=0; i<nums.length; i++) {
			val = target - nums[i];
			val_index = kv.getOrDefault(val, -1);
			if(val_index != -1 && i != val_index) {
				int[] result = {i, val_index};
				return result;
			}
			else {
				continue;
			}
		}
		
		return new int[2];
    }

}
