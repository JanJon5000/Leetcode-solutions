class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            find = arr[i]
            for j in range(i, len(arr)):
                if find / arr[j] == 2 or arr[j] / 2 == 2:
                    return True
            return False
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkIfExist([10, 5, 2, 3]))