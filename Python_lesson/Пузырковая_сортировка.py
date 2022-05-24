def mysort(nums):
    bomjur = True
    while bomjur:
        bomjur = False
        for item in range(len(nums) - 1):
            if nums[item] > nums[item + 1]:
                nums[item], nums[item + 1] = nums[item + 1], nums[item]
                bomjur = True

mylist = [1,4,6,7,8,4,4,2,252,6,457,48,5]
mysort(mylist)
print(mylist)