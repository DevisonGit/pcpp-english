class TimeInterval:
    def __init__(self, *, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.total_seconds = self._to_seconds()

    def _to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def _from_seconds(self, total_seconds):
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return hours, minutes, seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only add TimeInterval to TimeInterval")
        total_seconds = self.total_seconds + other.total_seconds
        hours, minutes, seconds = self._from_seconds(total_seconds)
        return TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only subtract TimeInterval from TimeInterval")
        total_seconds = self.total_seconds - other.total_seconds
        hours, minutes, seconds = self._from_seconds(total_seconds)
        return TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    def __mul__(self, multiplier):
        if not isinstance(multiplier, int):
            raise TypeError("Can only multiply TimeInterval by an integer")
        total_seconds = self.total_seconds * multiplier
        hours, minutes, seconds = self._from_seconds(total_seconds)
        return TimeInterval(hours=hours, minutes=minutes, seconds=seconds)


# Test data
fti = TimeInterval(hours=21, minutes=58, seconds=50)
sti = TimeInterval(hours=1, minutes=45, seconds=22)

# Expected results
addition_result = fti + sti
subtraction_result = fti - sti
multiplication_result = fti * 2

# Assert statements
assert str(addition_result) == "23:44:12"
assert str(subtraction_result) == "20:13:28"
assert str(multiplication_result) == "43:57:40"

# Print results
print(f"Addition Result: {addition_result}")          # Should print 23:44:12
print(f"Subtraction Result: {subtraction_result}")    # Should print 20:13:28
print(f"Multiplication Result: {multiplication_result}")  # Should print 43:57:40
