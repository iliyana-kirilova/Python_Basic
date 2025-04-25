spead = float(input())
if spead<=10:
    print('slow')
elif 10< spead<=50:
    print('average')
elif 50< spead<=150:
    print('fast')
elif 150 < spead <= 1000:
    print('ultra fast')
else:
    print('extremely fast')