class FileHandler:
    def read_input():
        with open("INPUT.TXT", "r") as file:
            return int(file.read().strip())

    def write_output(result):
        with open("OUTPUT.TXT", "w") as file:
            file.write(str(result))

class Validator:
    def validate(N):
        if N < 1 or N >= 33:
            raise ValueError("N must be a natural number less than 33.")

class Logic:
    def calculate_ways(N):
        if N % 2 != 0:
            return 0
        
        dp = [0] * (N + 1)
        dp[0] = 1  # Базовий випадок для порожньої плитки
        if N >= 2:
            dp[2] = 3  # Є 3 способи розділити плитку 3x2
        if N >= 4:
            dp[4] = 11  # Є 11 способів розділити плитку 3x4

        for i in range(6, N + 1, 2):
            dp[i] = 4 * dp[i - 2] - dp[i - 4]

        return dp[N]

def main():
    try:
        N = FileHandler.read_input()
        Validator.validate(N)
        
        result = Logic.calculate_ways(N)
        FileHandler.write_output(result)
        
        print(f"The number of ways to divide a 3x{N} chocolate bar: {result}")
    
    except ValueError as ex:
        print("Invalid input:", ex)
    except Exception as ex:
        print("An error occurred:", ex)

if __name__ == "__main__":
    main()
