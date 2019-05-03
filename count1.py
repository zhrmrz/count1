class Sol:
    def count1(self,num):
        sum=0
        for n in str(num):
            if n=='1':
                sum+=1
        return sum
if __name__ == '__main__':
    p1=Sol()
    print(p1.count1(1010))
