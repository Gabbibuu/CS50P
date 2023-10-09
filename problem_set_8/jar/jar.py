class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError("Deposit error")

    def withdraw(self, n):
        if n <= self.size:
            self.size -= n
        else:
            raise ValueError("Withdraw error")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("@capacity.setter error")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("@size.setter error")
        self._size = size


def main():
    jar = Jar()
    print(jar.capacity)

    print(jar)
    jar.deposit(3)
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(2)
    print(jar)
    jar.withdraw(1)
    print(jar)

    print(jar.size)


if __name__ == "__main__":
    main()
