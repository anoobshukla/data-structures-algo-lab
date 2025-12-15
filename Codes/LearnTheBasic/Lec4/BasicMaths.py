class BasicMaths:

    @staticmethod
    def countNumber(n):
        cnt = 0
        while n > 0:
            n = n//10
            cnt+=1
        return(cnt)
    
    @staticmethod
    def revNum(n):
        rev = 0
        while n >0 :
            digit = n%10
            rev = rev *10 + digit
            n = n//10
        return rev
    
    @staticmethod
    def pallindrome(n):
        if n == BasicMaths.revNum(n):
            return(f"Number {n} is a pallindrome number")
        else:
            return(f"Number {n} is not a pallindrome number")
  
    @staticmethod
    def armstrongNumber(n):
        dup = n
        sum = 0
        while n > 0:
            num = n % 10
            print(num)
            sum = sum + (num * num * num)
            print("num", sum)
            n = n//10
            # numCube += numCube

        # print(numCube)
        print("sum",sum)
        if sum != dup:
            return(f"Number {dup} is not a armstrong number")
        else:
            return(f"Number {dup} is an armstrong number")


    @staticmethod
    def optimisedFactors(n):
        lst = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                lst.append(i)
                # print("lst",lst)
                if i != n // i:        
                    lst.append(n // i)
        return sorted(lst)

    @staticmethod
    def primeNumber(n):
        cnt =0
        for i in range(1,n):
            if n%i == 0:
                cnt+=1
                print(cnt)
        if cnt > 2:
            return(f"Number {n} is not a Prime Number")
        else:
            return(f"Number {n} is  a Prime Number")

    @staticmethod
    def optimisedPrimeNum(n):
        cnt = 0
        for i in range(1,int(n ** 0.5 +1)):
            if n % i == 0 :
                cnt +=1
                if i != n//i :
                    cnt+=1
        # print("cnt",cnt)
        if cnt > 2:
            return(f"Number {n} is not a Prime Number")
        else:
            return(f"Number {n} is  a Prime Number")
        
    # @staticmethod
    # def gcdOrHcf(n1,n2):
    #     gcd = 0
    #     for i in range(1,min(n1,n2)+1):
    #         if(n1%i ==0 and n2%i ==0):
    #             gcd = i
    #     return gcd

    @staticmethod
    def gcdOrHcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a


# sol = BasicMaths.countNumber(45678)
# print(sol)
# rev = BasicMaths.revNum(456789)
# print(rev)
# isPallindrome = BasicMaths.pallindrome(7)
# print(isPallindrome)
# isArmstrong = BasicMaths.armstrongNumber(143)
# print(isArmstrong)
# allFactors = BasicMaths.optimisedFactors(36)
# print(allFactors)
# primeNumber = BasicMaths.primeNumber(51)
# print(primeNumber)
# primeNumber = BasicMaths.optimisedPrimeNum(18)
# print(primeNumber)
gcd = BasicMaths.gcdOrHcf(6,12)
print(gcd)
