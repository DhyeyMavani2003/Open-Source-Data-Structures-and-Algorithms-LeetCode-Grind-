class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}  # Dictionary to store tokenId and its expiration time

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        # Check if tokenId exists and hasn't expired yet
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(1 for expiry in self.tokens.values() if expiry > currentTime)

# Testing the AuthenticationManager class
obj = AuthenticationManager(10)
obj.generate("token1", 1)
obj.generate("token2", 2)
obj.renew("token1", 5)
count = obj.countUnexpiredTokens(10)
count
