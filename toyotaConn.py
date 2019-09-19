nums = "12234567"
answr = ""
for i in range(len(nums)-1):
    if int(nums[i]) % 2 == 0 and int(nums[i+1]) % 2 == 0:
        answr += nums[i] + "*" + nums[i+1]
    elif int(nums[i]) % 2 != 0 and int(nums[i+1]) % 2 != 0:
        answr += nums[i] + "-" + nums[i+1]
    else:
        answr += nums[i]
answr += nums[-1]
print(answr)


