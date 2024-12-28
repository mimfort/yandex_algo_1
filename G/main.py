def calculate_details(N, K, M):
    if M > K:
        return 0

    total_details = 0

    while N >= K:
        blanks = N // K
        leftover_after_blanks = N % K

        details_from_blanks = (K // M) * blanks
        leftover_after_details = (K % M) * blanks

        N = leftover_after_blanks + leftover_after_details
        total_details += details_from_blanks

    return total_details


N, K, M = map(int, input().split())


print(calculate_details(N, K, M))
