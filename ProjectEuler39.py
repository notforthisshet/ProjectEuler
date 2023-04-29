# Integer right triangles
import time
start = time.time()
mx = 0
max_length = 0
for p in range(0, 1001, 2):
    print(p)
    sols = 0
    for a in range(1, p):
        if p == 0:
            break
        for b in range(1, p - a):
            c = (a ** 2 + b ** 2) ** 0.5
            if a + b + c == p:
                sols += 1
    if sols // 2 > max_length:
        max_length = sols // 2
        mx = p
end = time.time()
total = end - start
print(f"Time elapsed: {total:.5f} seconds")  # 30 seconds T-T I don't know how to make it faster
print(mx)  # Output: 840
