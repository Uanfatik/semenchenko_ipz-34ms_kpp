import os

class Logic:
    def process(input_str):
        if not Validator.validate_input(input_str):
            return 0, 0

        N, K1, K2, S = Validator.parse_input(input_str)

        dp = [[0.0 for _ in range(N + 1)] for _ in range(N + 1)]
        dp[K1][K2] = 1.0

        for i in range(K1, N):
            for j in range(K2, N):
                if dp[i][j] > 0:
                    dp[i + 1][j] += dp[i][j] * 0.5
                    dp[i][j + 1] += dp[i][j] * 0.5

        petya_win_prob = sum(dp[N][j] for j in range(N))
        vasya_win_prob = sum(dp[i][N] for i in range(N))

        petya_coins = int(petya_win_prob / (petya_win_prob + vasya_win_prob) * S)
        vasya_coins = S - petya_coins

        return petya_coins, vasya_coins


class Validator:
    def validate_input(input_str):
        try:
            N, K1, K2, S = map(int, input_str.split())
            if not (1 <= N <= 50 and 0 <= K1 < N and 0 <= K2 < N and 1 < S < 10**100):
                return False
            return True
        except ValueError:
            return False


    def parse_input(input_str):
        return map(int, input_str.split())


def main():
    try:
        with open("Input.txt", "r") as file:
            input_data = file.read().strip()

        petya_coins, vasya_coins = Logic.process(input_data)

        with open("Output.txt", "w") as file:
            file.write(f"{petya_coins} {vasya_coins}")

        print(f"Petya's coins: {petya_coins}, Vasya's coins: {vasya_coins}")
    
    except FileNotFoundError as ex:
        print(f"File not found: {ex}")
    except ValueError as ex:
        print(f"Invalid format: {ex}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    main()
