# 연습문제 1: 1부터 100까지 더하기
sum = 0
while i <= 100:
    sum += i
    i += 1 
print(sum)

# 연습문제 2: 3의 배수의 합 
sum = 0
while i < 1000:
    if i % 3 == 0:
        sum += i
        i += 1
    else:
        i += 1
print(sum)

# 그런데 3의 배수든 아니든 1씩 증가해야 하므로
sum = 0
while i < 1000:
    if i % 3 == 0:
        sum += i
    i += 1
# 이라고 작성하는 것이 더 간결하다. 
# 약간 computational thinking 자체가 몸에 배지 않아서 애매하게 기계적으로 생각하고 있는 것 같은데,
# if 에서 말 그대로 "if" 이 친구가 3의 배수인지 아닌지 확인하고 그게 아니면 
# i += 1만 실행하는 것이기 때문에 굳이 else를 적어줄 필요가 없다.
# 모로 가도 서울만 가면 된다고는 하지만, 확실히 반복되는 부분은 정말 필요한 반복인지 혹은
# 더 간결하게 만들 수 있는 반복인지 확인이 필요하다. 

# 연습문제 3: 50점 이상의 총합
A = [20, 55, 67. 82, 45, 33, 90, 87, 100, 25]
sum = 0
i = 0
while i < len(A):
    if A[i] >= 50:
        sum += A[i]
    i += 1
print(sum)

# for문 전에 while문을 배우기 때문에, for문을 쓰지않고 while로만 쓰려고 하니까
# 막상 잘 생각이 안나서 조금 고민이 되었다. 
# 연습문제 해설에서는 pop을 이용해서 푸는데, 신선하게 느껴졌다.
# 문자열, 리스트 등 전반부에서 많은 함수들을 배웠지만 간단히 예제를 따라하는 정도라서
# 실질적으로 어떻게 쓰일 수 있는지는 확 와닿지 않기 때문이다.

# 연습문제 4: 별 표시하기 1
i = 0
while i < 5:
    print("*" * i)
    i += 1 

# 연습문제 5: 별 표시하기 2
i = 7
while i > 0:
    print("{0:^7}".format("*" * i))
    i -= 2

