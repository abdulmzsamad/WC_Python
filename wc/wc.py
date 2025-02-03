class WC:
    def __init__(self, file):
        self.file = file  # Accept the file object here
        self.bytes = 0
        self.lines = 0
        self.words = 0
        self.characters = 0

    def count_bytes(self):
        """Count the total bytes in the file."""
        self.bytes = len(self.file.read())

    def count_lines(self):
        """Count the total lines in the file."""
        self.file.seek(0)  # Reset file pointer to beginning
        self.lines = sum(1 for line in self.file)

    def count_words(self):
        """Count the words in the file."""
        self.file.seek(0)  # Reset file pointer to beginning
        in_word = False
        for c in self.file.read():
            if chr(c).isspace():
                in_word = False
            elif not in_word:
                self.words += 1
                in_word = True

    def count_characters(self):
        """Count characters, including multi-byte UTF-8 characters."""
        self.file.seek(0)  # Reset file pointer to beginning
        self.characters = 0
        while True:
            c = self.file.read(1)
            if not c:
                break
            if (c[0] & 0x80) == 0:  # Single-byte character
                self.characters += 1
            else:
                continuation_bytes = self.get_utf8_bytes(c[0])
                self.characters += 1
                for _ in range(continuation_bytes):
                    continuation_byte = self.file.read(1)
                    if not continuation_byte:
                        break

    def get_utf8_bytes(self, c):
        """Helper method to calculate UTF-8 continuation bytes."""
        if (c & 0xE0) == 0xC0:
            return 1
        elif (c & 0xF0) == 0xE0:
            return 2
        elif (c & 0xF8) == 0xF0:
            return 3
        return 0

    def calculate_stats(self):
        """Coordinator method to perform all counting tasks."""
        self.count_bytes()
        self.count_lines()
        self.count_words()
        self.count_characters()
    