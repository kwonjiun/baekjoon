n = int(input())

dp = [1,1,1]

mod = 9901

for i in range(1,n):
    fisrt = dp[0]
    second = dp[1]
    empty = dp[2]
    dp[0] = (second + empty) % mod
    dp[1] = (fisrt + empty) %mod
    dp[2] = (fisrt+second+empty) % mod
print(sum(dp)%mod)